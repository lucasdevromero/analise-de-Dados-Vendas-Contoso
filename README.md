# Análise de Vendas da Contoso - 2017

Este projeto realiza uma análise detalhada dos dados de vendas da empresa Contoso para o ano de 2017. Utilizando a biblioteca Pandas do Python, o script processa, limpa e mescla diferentes fontes de dados para extrair insights valiosos sobre faturamento, lucro, produtos mais vendidos, desempenho por loja e por país.

## 📁 Estrutura do Projeto

O projeto é composto pelo script principal e pelos arquivos de dados necessários:

  - `Analise_de_dados_Vendas_Contoso.py`: O script Python que contém todo o código para a análise.
  - `Contoso - Vendas - 2017.csv`: Arquivo com os dados detalhados de cada venda realizada em 2017.
  - `Contoso - Lojas.csv`: Arquivo com o cadastro e informações das lojas da rede.
  - `Contoso - Cadastro Produtos.csv`: Arquivo com o cadastro e informações dos produtos.

## 🚀 Como Executar

Para executar a análise, siga os passos abaixo:

### Pré-requisitos

  - Python 3.x instalado
  - Biblioteca Pandas instalada

Caso não tenha o Pandas, instale-o com o seguinte comando:

```bash
pip install pandas
```

### Execução

1.  Certifique-se de que o script `Analise_de_dados_Vendas_Contoso.py` e os três arquivos `.csv` estejam no mesmo diretório.
2.  Execute o script através de um terminal ou de uma IDE compatível com Python (como Jupyter Notebook, VS Code, etc.).

## 🛠️ Etapas da Análise

O script realiza as seguintes etapas de processamento e análise:

1.  **Carregamento dos Dados**: Importa os três arquivos CSV (`Vendas`, `Lojas` e `Produtos`) para DataFrames do Pandas.

2.  **Tratamento e Limpeza**:

      - Converte as colunas de data (`Data da Venda`, `Data do Envio`) para o formato datetime.
      - Mescla os três DataFrames em um único DataFrame consolidado (`df_merge_contoso`) para facilitar a análise.
      - Converte colunas de valores monetários (`Custo Unitario`, `Preco Unitario`), que estavam como texto, para o formato numérico (float).
      - Trata valores ausentes (`NaN`) na coluna `Quantidade Colaboradores`, substituindo-os por 0.

3.  **Engenharia de Features**:

      - Cria novas colunas calculadas para enriquecer a análise:
          - `Lucro_Unitario`: Diferença entre o preço e o custo unitário.
          - `Faturamento_Total`: Preço unitário multiplicado pela quantidade vendida.
          - `Lucro_Total`: Lucro unitário multiplicado pela quantidade vendida.
          - `mes`: Extrai o nome do mês da `Data da Venda`.

4.  **Análise de Negócio**: Responde a perguntas-chave para gerar insights, como:

      - Qual foi o faturamento total em 2017?
      - Quais as 5 marcas mais vendidas em quantidade?
      - Qual o mês com maior volume de vendas (em faturamento e quantidade)?
      - Qual loja obteve o maior faturamento e lucro?
      - Qual país gerou o maior valor de faturamento e lucro?

## 📈 Principais Insights Obtidos

A análise revelou os seguintes pontos principais sobre o desempenho da Contoso em 2017:

  - **Mês de Maior Performance**: **Novembro** foi o mês com o maior faturamento, atingindo **$ 318.624.488,87**, e também o mês com a maior quantidade de peças vendidas (1.143.531).

  - **Loja Destaque**: A **Loja Contoso Catalog** foi a líder em desempenho, com o maior faturamento (**$ 277.058.181,11**) e o maior lucro (**$ 160.460.918,27**).

  - **País com Melhor Desempenho**: Os **Estados Unidos** se destacaram como o país com o maior faturamento (**$ 1.930.946.918,69**) e o maior lucro (**$ 1.116.661.706,08**).
