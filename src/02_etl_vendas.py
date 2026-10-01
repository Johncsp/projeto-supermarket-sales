import pandas as pd
from config import engine

ARQUIVO_TRATADO = "./data/processed/vendas_tratadas.csv"


def processar_vendas():
    print("Iniciando processamento dos dados...")

    df_raw_vendas = pd.read_sql(
        """
        SELECT *
        FROM raw_vendas
        """,
        engine
    )

    print("Dados carregados da tabela raw_vendas.")
    print("Total de registros:", len(df_raw_vendas))

    # Remover duplicidades pelo identificador da venda
    df_vendas_tratadas = df_raw_vendas.copy()

    duplicados = df_vendas_tratadas.duplicated(
        subset=["invoice_id"]
    ).sum()

    df_vendas_tratadas = df_vendas_tratadas.drop_duplicates(
        subset=["invoice_id"]
    ).copy()

    print("Duplicados removidos:", duplicados)
    print("Registros após remoção:", len(df_vendas_tratadas))

    # Padronizar textos
    colunas_texto = [
        "branch",
        "city",
        "customer_type",
        "gender",
        "product_line",
        "payment",
    ]

    for coluna in colunas_texto:
        df_vendas_tratadas[coluna] = (
            df_vendas_tratadas[coluna].str.strip()
        )

    # Converter data
    df_vendas_tratadas["date"] = pd.to_datetime(
        df_vendas_tratadas["date"],
        format="%m/%d/%Y",
        errors="coerce"
    )

    # Converter hora
    df_vendas_tratadas["time"] = pd.to_datetime(
        df_vendas_tratadas["time"],
        format="%I:%M:%S %p",
        errors="coerce"
    ).dt.time

    print(
        "Valores de data inválidos:",
        df_vendas_tratadas["date"].isna().sum()
    )

    print(
        "Valores de hora inválidos:",
        df_vendas_tratadas["time"].isna().sum()
    )

    # Renomear colunas
    df_vendas_tratadas = df_vendas_tratadas.rename(
        columns={
            "invoice_id": "id_venda",
            "branch": "filial",
            "city": "cidade",
            "customer_type": "tipo_cliente",
            "gender": "genero",
            "product_line": "linha_produto",
            "unit_price": "preco_unitario",
            "quantity": "quantidade",
            "tax_5_percent": "imposto",
            "sales": "valor_total",
            "date": "data_venda",
            "time": "hora_venda",
            "payment": "forma_pagamento",
            "cogs": "custo_mercadoria",
            "gross_margin_percentage": "margem_percentual",
            "gross_income": "receita_bruta",
            "rating": "avaliacao",
        }
    )

    # Verificações finais
    print("\nTotal de registros:", len(df_vendas_tratadas))
    print(
        "Invoice IDs duplicados:",
        df_vendas_tratadas["id_venda"].duplicated().sum()
    )

    # Exportar CSV tratado
    df_vendas_tratadas.to_csv(
        ARQUIVO_TRATADO,
        index=False
    )

    print("\nArquivo tratado gerado:", ARQUIVO_TRATADO)

    # Carregar tabela tratada no PostgreSQL
    df_vendas_tratadas.to_sql(
        "vendas_tratadas",
        engine,
        if_exists="replace",
        index=False
    )

    print("Dados gravados na tabela vendas_tratadas.")

    return df_vendas_tratadas


if __name__ == "__main__":
    processar_vendas()