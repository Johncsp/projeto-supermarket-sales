# Projeto Avaliativo - Análise de Dados de Vendas de Supermercado

---

## Sobre este projeto

O objetivo deste projeto foi desenvolver um fluxo introdutório de análise de dados utilizando PostgreSQL, SQL, Python e Pandas.

A partir da base pública **Supermarket Sales**, foram realizados o armazenamento dos dados brutos, o tratamento dos dados, a análise exploratória e a geração de métricas e gráficos para responder perguntas de negócio.

---

## Estrutura do projeto

```text
projeto-supermarket-sales/
│
├── data/
│   ├── raw/
│   │   └── supermarket_analysis.csv
│   └── processed/
│       └── vendas_tratadas.csv
│
├── resultados/
│   ├── estatisticas/
│   │   └── metricas.csv
│   └── graficos/
│       ├── faturamento_filiais.png
│       └── avaliacao_produtos.png
│
├── sql/
│   ├── 01_criar_banco.sql
│   ├── 02_criar_tabelas.sql
│   └── 03_consultas.sql
│
├── src/
│   ├── config.py
│   ├── 01_leitura_dados.py
│   ├── 02_etl_vendas.py
│   └── 03_estatistica.py
│
├── notebooks/
│   └── projeto_etl_completo.ipynb
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Arquivos principais

### SQL

- **01_criar_banco.sql:** criação do banco `dw_supermercado`.
- **02_criar_tabelas.sql:** criação das tabelas `raw_vendas` e `vendas_tratadas`.
- **03_consultas.sql:** consultas SQL utilizadas para extração e análise dos dados.

### Python

- **01_leitura_dados.py:** leitura e inspeção inicial do arquivo CSV e carga dos dados brutos no PostgreSQL.
- **02_etl_vendas.py:** tratamento, padronização, conversão de tipos, verificação de dados e geração da base tratada.
- **03_estatistica.py:** análise estatística, respostas às perguntas de negócio, geração dos gráficos e arquivo de métricas.
- **config.py:** configuração da conexão com o PostgreSQL utilizando variáveis do arquivo `.env`.

### Resultados

- **metricas.csv:** reúne as principais respostas obtidas na análise.
- **faturamento_filiais.png:** gráfico de faturamento por filial.
- **avaliacao_produtos.png:** gráfico de avaliação média por linha de produto.

---

## Como rodar o projeto

### 1. Pré-requisitos

É necessário ter instalado:

- Python
- PostgreSQL
- Git

### 2. Instalar as dependências

Na pasta do projeto, execute:

```bash
pip install -r requirements.txt
```

### 3. Configurar as credenciais

Criar um arquivo `.env` na raiz do projeto:

```text
DB_USER=postgres
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432
DB_NAME=dw_supermercado
```

### 4. Criar o banco

Executar o arquivo no Dbeaver:

```text
sql/01_criar_banco.sql
```

Depois executar no Dbeaver:

```text
sql/02_criar_tabelas.sql
```

### 5. Executar a leitura e carga dos dados

Na raiz do projeto:

```bash
python src/01_leitura_dados.py
```

Esse processo realiza a leitura do CSV original e carrega os dados na tabela `raw_vendas`.

### 6. Executar o tratamento

```bash
python src/02_etl_vendas.py
```

Esse processo realiza o tratamento dos dados e gera:

```text
data/processed/vendas_tratadas.csv
```

Também realiza a carga da tabela `vendas_tratadas`.

### 7. Executar as análises

```bash
python src/03_estatistica.py
```

Ao final serão gerados:

```text
resultados/estatisticas/metricas.csv
resultados/graficos/faturamento_filiais.png
resultados/graficos/avaliacao_produtos.png
```

---

## Perguntas de negócio respondidas

A análise responde às seguintes perguntas:

1. Qual filial teve o maior faturamento?
2. Qual filial teve mais vendas?
3. Qual linha de produto teve o maior faturamento?
4. Qual linha de produto teve a melhor avaliação média?
5. Qual foi a forma de pagamento mais utilizada?
6. Qual foi o valor médio das vendas?
7. Qual foi a maior venda?
8. Qual dia da semana teve mais vendas?

---

## Resultados da análise

Os resultados obtidos no notebook e reproduzidos pelo `03_estatistica.py` foram:

- **Filial com maior faturamento:** Giza — aproximadamente R$ 110.568,71.
- **Filial com mais vendas:** Alex — 340 vendas.
- **Linha de produto com maior faturamento:** Food and beverages — aproximadamente R$ 56.144,84.
- **Linha de produto com melhor avaliação média:** Food and beverages — aproximadamente 7,11.
- **Forma de pagamento mais utilizada:** E-wallet — 345 vendas.
- **Valor médio das vendas:** aproximadamente R$ 322,97.
- **Maior venda:** R$ 1.042,65.
- **Dia da semana com mais vendas:** Saturday — 164 vendas.

---

## Notebook

O notebook utilizado durante o desenvolvimento contém as etapas de leitura, análise exploratória, tratamento, análise estatística e geração dos resultados.

```text
notebooks/projeto_etl_completo.ipynb
```

O notebook foi utilizado como ambiente de desenvolvimento e validação. Os códigos finais foram organizados nos arquivos Python da pasta `src/`.
