
-- ============================================================
-- TABELA raw_vendas
-- Armazena os dados do arquivo original.
-- Padronizado nomes das colunas em minusculo sem espaço
-- ============================================================
CREATE TABLE raw_vendas (
    invoice_id VARCHAR(50) PRIMARY KEY,
    branch VARCHAR(10) NOT NULL,
    city VARCHAR(100) NOT NULL,
    customer_type VARCHAR(50),
    gender VARCHAR(20),
    product_line VARCHAR(150) NOT NULL,
    unit_price NUMERIC(10, 2),
    quantity INTEGER,
    tax_5_percent NUMERIC(10, 2),
    sales NUMERIC(12, 2),
    date VARCHAR(20),
    time VARCHAR(20),
    payment VARCHAR(50),
    cogs NUMERIC(12, 2),
    gross_margin_percentage NUMERIC(10, 2),
    gross_income NUMERIC(12, 2),
    rating NUMERIC(4, 2)
);

-- ============================================================
-- TABELA vendas_tratadas - Armazena os dados após o processo de tratamento.
-- ============================================================

CREATE TABLE vendas_tratadas (
    id_venda VARCHAR(50) PRIMARY KEY NOT NULL,
    filial VARCHAR(10) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    tipo_cliente VARCHAR(50),
    genero VARCHAR(20),
    linha_produto VARCHAR(150) NOT NULL,
    preco_unitario NUMERIC(10, 2) CHECK (preco_unitario >= 0),
    quantidade INTEGER CHECK (quantidade > 0),
    imposto NUMERIC(10, 2) CHECK (imposto >= 0),
    valor_total NUMERIC(12, 2) CHECK (valor_total >= 0),
    data_venda DATE,
    hora_venda TIME,
    forma_pagamento VARCHAR(50) NOT NULL,
    custo_mercadoria NUMERIC(12, 2) CHECK (custo_mercadoria >= 0),
    margem_percentual NUMERIC(10, 2),
    receita_bruta NUMERIC(12, 2) CHECK (receita_bruta >= 0),
    avaliacao NUMERIC(4, 2) CHECK (avaliacao BETWEEN 0 AND 10)
);