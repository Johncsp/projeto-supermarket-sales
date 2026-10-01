import pandas as pd
import matplotlib.pyplot as plt

ARQUIVO_TRATADO = "data/processed/vendas_tratadas.csv"
ARQUIVO_METRICAS = "resultados/estatisticas/metricas.csv"

def analisar_vendas():
    print("Iniciando análise estatística...")

    # A análise utiliza o arquivo CSV tratado
    df_analise = pd.read_csv(ARQUIVO_TRATADO)

    print("Dados tratados carregados.")
    print("Total de registros:", len(df_analise))

    # Tabela para armazenar as métricas
    df_metricas = pd.DataFrame(
        columns=["metrica", "resultado", "valor"]
    )

    # 1. Filial com maior faturamento
    faturamento_filial = (
        df_analise
        .groupby("filial")["valor_total"]
        .sum()
        .sort_values(ascending=False)
    )

    filial_maior_faturamento = faturamento_filial.index[0]
    valor_maior_faturamento = faturamento_filial.iloc[0]

    print(
        "\nFilial com maior faturamento:",
        filial_maior_faturamento,
        "-",
        round(valor_maior_faturamento, 2)
    )

    df_metricas.loc[len(df_metricas)] = [
        "maior_faturamento_filial",
        filial_maior_faturamento,
        valor_maior_faturamento,
    ]

    # 2. Filial com maior quantidade de vendas
    quantidade_filial = (
        df_analise["filial"]
        .value_counts()
    )

    filial_maior_quantidade = quantidade_filial.index[0]
    valor_maior_quantidade = quantidade_filial.iloc[0]

    print(
        "Filial com maior quantidade de vendas:",
        filial_maior_quantidade,
        "-",
        valor_maior_quantidade
    )

    df_metricas.loc[len(df_metricas)] = [
        "maior_quantidade_vendas_filial",
        filial_maior_quantidade,
        valor_maior_quantidade,
    ]

    # 3. Linha de produto com maior faturamento
    faturamento_produto = (
        df_analise
        .groupby("linha_produto")["valor_total"]
        .sum()
        .sort_values(ascending=False)
    )

    produto_maior_faturamento = faturamento_produto.index[0]
    valor_produto_maior_faturamento = faturamento_produto.iloc[0]

    print(
        "Linha de produto com maior faturamento:",
        produto_maior_faturamento,
        "-",
        round(valor_produto_maior_faturamento, 2)
    )

    df_metricas.loc[len(df_metricas)] = [
        "maior_faturamento_linha_produto",
        produto_maior_faturamento,
        valor_produto_maior_faturamento,
    ]

    # 4. Linha de produto com melhor avaliação média
    avaliacao_produto = (
        df_analise
        .groupby("linha_produto")["avaliacao"]
        .mean()
        .sort_values(ascending=False)
    )

    produto_melhor_avaliacao = avaliacao_produto.index[0]
    valor_melhor_avaliacao = avaliacao_produto.iloc[0]

    print(
        "Linha de produto com melhor avaliação média:",
        produto_melhor_avaliacao,
        "-",
        round(valor_melhor_avaliacao, 2)
    )

    df_metricas.loc[len(df_metricas)] = [
        "melhor_avaliacao_linha_produto",
        produto_melhor_avaliacao,
        valor_melhor_avaliacao,
    ]

    # 5. Forma de pagamento mais utilizada
    pagamentos = df_analise["forma_pagamento"].value_counts()

    pagamento_mais_utilizado = pagamentos.index[0]
    quantidade_pagamento = pagamentos.iloc[0]

    print(
        "Forma de pagamento mais utilizada:",
        pagamento_mais_utilizado,
        "-",
        quantidade_pagamento
    )

    df_metricas.loc[len(df_metricas)] = [
        "forma_pagamento_mais_utilizada",
        pagamento_mais_utilizado,
        quantidade_pagamento,
    ]

    # 6. Valor médio das vendas
    valor_medio = df_analise["valor_total"].mean()

    print(
        "Valor médio das vendas:",
        round(valor_medio, 2)
    )

    df_metricas.loc[len(df_metricas)] = [
        "valor_medio_vendas",
        "valor médio",
        valor_medio,
    ]

    # 7. Maior venda registrada
    maior_venda = df_analise["valor_total"].max()

    print(
        "Maior venda registrada:",
        round(maior_venda, 2)
    )

    df_metricas.loc[len(df_metricas)] = [
        "maior_venda",
        "maior venda",
        maior_venda,
    ]

    # 8. Dia da semana com maior quantidade de vendas
    df_analise["data_venda"] = pd.to_datetime(
        df_analise["data_venda"]
    )

    df_analise["dia_semana"] = (
        df_analise["data_venda"].dt.day_name()
    )

    vendas_dia = (
        df_analise["dia_semana"]
        .value_counts()
    )

    dia_maior_quantidade = vendas_dia.index[0]
    quantidade_dia = vendas_dia.iloc[0]

    print(
        "Dia da semana com maior quantidade de vendas:",
        dia_maior_quantidade,
        "-",
        quantidade_dia
    )

    df_metricas.loc[len(df_metricas)] = [
        "maior_quantidade_vendas_dia_semana",
        dia_maior_quantidade,
        quantidade_dia,
    ]

    # Salvar métricas
    df_metricas.to_csv(
        ARQUIVO_METRICAS,
        index=False,
    encoding="utf-8"
    )

    print("\nArquivo de métricas gerado:", ARQUIVO_METRICAS)

    # Gráfico: faturamento por filial
    plt.figure(figsize=(8, 5))
    faturamento_filial.plot(kind="bar")
    plt.title("Faturamento por filial")
    plt.xlabel("Filial")
    plt.ylabel("Faturamento")
    plt.tight_layout()
    plt.savefig("./resultados/graficos/faturamento_filiais.png")
    plt.close()

    # Gráfico: avaliação média por linha de produto
    plt.figure(figsize=(10, 6))
    avaliacao_produto.sort_values().plot(kind="barh")
    plt.title("Avaliação média por linha de produto")
    plt.xlabel("Avaliação média")
    plt.ylabel("Linha de produto")
    plt.tight_layout()
    plt.savefig("./resultados/graficos/avaliacao_produtos.png")
    plt.close()

    print("Gráficos gerados.")
    print("\nAnálise estatística concluída.")


if __name__ == "__main__":
    analisar_vendas()
