-- 1. Extração dos dados brutos para o Python
SELECT *
FROM raw_vendas;


-- 2. Consulta com filtro: vendas acima de 500
SELECT
    invoice_id,
    branch,
    city,
    product_line,
    sales
FROM raw_vendas
WHERE sales > 500
ORDER BY sales DESC;


-- 3. Quantidade de vendas e faturamento por filial
SELECT
    branch,
    COUNT(*) AS quantidade_vendas,
    SUM(sales) AS faturamento_total,
    AVG(sales) AS valor_medio
FROM raw_vendas
GROUP BY branch
ORDER BY faturamento_total DESC;


-- 4. Faturamento e avaliação média por linha de produto
SELECT
    product_line,
    SUM(sales) AS faturamento_total,
    AVG(rating) AS avaliacao_media
FROM raw_vendas
GROUP BY product_line
ORDER BY faturamento_total DESC;


-- 5. Quantidade de vendas por forma de pagamento
SELECT
    payment,
    COUNT(*) AS quantidade_vendas,
    SUM(sales) AS faturamento_total
FROM raw_vendas
GROUP BY payment
ORDER BY quantidade_vendas DESC;


-- 6. Estatísticas gerais das vendas
SELECT
    COUNT(*) AS quantidade_vendas,
    SUM(sales) AS faturamento_total,
    AVG(sales) AS valor_medio,
    MAX(sales) AS maior_venda,
    MIN(sales) AS menor_venda
FROM raw_vendas;