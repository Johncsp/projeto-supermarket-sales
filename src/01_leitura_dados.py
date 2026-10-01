import pandas as pd
from config import engine

ARQUIVO_RAW = "./data/raw/supermarket_analysis.csv"


def ler_dados():
    print("Lendo dados do arquivo CSV...")

    df_vendas = pd.read_csv(ARQUIVO_RAW)

    df_vendas.columns = [
        "invoice_id",
        "branch",
        "city",
        "customer_type",
        "gender",
        "product_line",
        "unit_price",
        "quantity",
        "tax_5_percent",
        "sales",
        "date",
        "time",
        "payment",
        "cogs",
        "gross_margin_percentage",
        "gross_income",
        "rating",
    ]

    print("Dados carregados com sucesso.")
    print("Quantidade de registros:", len(df_vendas))

    df_vendas.to_sql(
        "raw_vendas",
        engine,
        if_exists="replace",
        index=False
    )

    print("\nDados gravados na tabela raw_vendas.")
    return df_vendas


if __name__ == "__main__":
    ler_dados()
