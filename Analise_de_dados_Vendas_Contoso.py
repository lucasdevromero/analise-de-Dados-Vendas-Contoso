#!/usr/bin/env python
# coding: utf-8

# In[110]:


import pandas as pd


# In[111]:


df_contoso_vendas_2017 = pd.read_csv('Contoso - Vendas - 2017.csv', sep=';')
df_contoso_lojas = pd.read_csv('Contoso - Lojas.csv', sep=';')
df_contoso_produtos = pd.read_csv('Contoso - Cadastro Produtos.csv', sep=';')
#display(df_contoso_vendas_2017)
#display(df_contoso_lojas)


# ### Tratamento

# In[112]:


print(df_contoso_vendas_2017.dtypes)
#identificamos que as colunas de data estão como object e vamos trata-las para que seja em formato de data
#também identificamos que nenhuma das colunas tem valor NaN


# In[113]:


df_contoso_vendas_2017["Data da Venda"] = pd.to_datetime(df_contoso_vendas_2017["Data da Venda"], dayfirst=True)
df_contoso_vendas_2017["Data do Envio"] = pd.to_datetime(df_contoso_vendas_2017["Data do Envio"], dayfirst=True)
print(df_contoso_vendas_2017.dtypes)


# In[114]:


df_merge_contoso = pd.merge(df_contoso_vendas_2017, df_contoso_lojas, on='ID Loja', how='inner')
df_merge_contoso = pd.merge(df_merge_contoso, df_contoso_produtos, on='ID Produto', how='inner')


# ##Desafios iniciais — Leitura e primeiros insights
# 
# ### Quantas linhas e colunas tem sua base?
# Dica: investigue o shape.
# 
# ### Quais os tipos de dados (dtypes) de cada coluna?
# Alguma coluna de data ainda está como object?
# 
# Existem valores nulos? Em quais colunas? Quantos?
# Extra: existe alguma coluna com muitos valores ausentes?
# 
# ------------------
# 

# In[115]:


#Quantas linhas e colunas tem sua base?
print(df_merge_contoso.shape)

#Quais os tipos de dados (dtypes) de cada coluna?
print(df_merge_contoso.dtypes)
#tranformando colunas de preços em float
df_merge_contoso["Custo Unitario"] = df_merge_contoso["Custo Unitario"].str.replace(",", ".")  # troca vírgula por ponto
df_merge_contoso["Custo Unitario"] = df_merge_contoso["Custo Unitario"].str.strip()  # tira espaços em branco
df_merge_contoso["Custo Unitario"] = pd.to_numeric(df_merge_contoso["Custo Unitario"], errors="coerce")
df_merge_contoso["Preco Unitario"] = df_merge_contoso["Preco Unitario"].str.replace(",", ".")  # troca vírgula por ponto
df_merge_contoso["Preco Unitario"] = df_merge_contoso["Preco Unitario"].str.strip()  # tira espaços em branco
df_merge_contoso["Preco Unitario"] = pd.to_numeric(df_merge_contoso["Preco Unitario"], errors="coerce")
print(df_merge_contoso.dtypes)


# In[116]:


#Criando uma coluna de Lucro Unitário
df_merge_contoso["Lucro_Unitario"] = df_merge_contoso["Preco Unitario"] - df_merge_contoso["Custo Unitario"]
df_merge_contoso["Faturamento_Total"] = df_merge_contoso["Preco Unitario"] * df_merge_contoso["Quantidade Vendida"]
df_merge_contoso["Lucro_Total"] = df_merge_contoso["Lucro_Unitario"] * df_merge_contoso["Quantidade Vendida"]
display(df_merge_contoso)


# 📈 Desafios de análise de vendas
# 
# ### Qual foi o total de vendas (Faturamento) em 2017?
# Multiplique a quantidade vendida pelo preço unitário (se houver as colunas).
# 
# ### Quais os 5 marcas mais vendidas em quantidade?
# Extra: quanto cada um faturou?
# 
# ### Qual foi o mês com maior volume de vendas?
# Dica: você vai precisar converter a coluna de data corretamente e agrupar por mês.
# 
# ------------------

# In[117]:


#Qual foi o total de vendas (Faturamento) em 2017?
total_faturamento = df_merge_contoso["Faturamento_Total"].sum()
print("O total de faturamento é $ {:,.2f}".format(total_faturamento))


# In[118]:


#Quais os 5 marcas mais vendidas em quantidade?
quantidade_agrupadas = df_merge_contoso.groupby("Nome da Marca")["Quantidade Vendida"].sum()
quantidade_ordenadas = vendas_agrupadas.sort_values(ascending=False)
top_5_produtos = vendas_ordenadas.head(5)

print("Top 5 produtos com maiores quantidades vendidas:")
for produto, quantidade in top_5_produtos.items():
    print(f"{produto}: {quantidade:,}")


# In[128]:


#Qual foi o mês com maior volume de vendas?
df_merge_contoso['mes'] = df_merge_contoso['Data da Venda'].dt.month_name()

# Agrupar e somar faturamento, ordenando pelo mês
vendas_por_mes = df_merge_contoso.groupby('mes')['Faturamento_Total'].sum()
peças_por_mes = df_merge_contoso.groupby('mes')['Quantidade Vendida'].sum()

mes_top = vendas_por_mes.idxmax()
faturamento_top = vendas_por_mes.max()
mes_top_peças = peças_por_mes.idxmax()
peças_top = peças_por_mes.max()

print(f"O mês com maior faturamento foi {mes_top} com R$ {faturamento_top:,.2f}")
print(f"E o mês que teve a maior quantidade de peças vendidas {mes_top_peças} com {peças_top:,}")


# 🏢 Desafios de análise por loja ou região
# 
# ### Qual loja vendeu mais em faturamento e obteve mais lucro?
# E qual vendeu menos?
# 
# ### Qual Pais teve maior valor de faturamento e lucro?
# Agrupe por estado e ordene.
# 
# ----------------------

# In[120]:


#Antes de trazer as lojas com mais faturamento, verificamos que a coluna Quantidade Colaboradores tem valores NaN e vamos trata-los
print(df_merge_contoso.isnull().sum())


# In[121]:


#Tratamento
df_merge_contoso["Quantidade Colaboradores"] = df_merge_contoso["Quantidade Colaboradores"].fillna(0)
print(df_merge_contoso.isnull().sum())


# In[122]:


#Qual loja vendeu mais em faturamento e obteve mais lucro?
# Agrupar e somar faturamento
df_merge_contoso.rename(columns={'Nome da Loja': 'Nome_da_Loja'}, inplace=True)
vendas_por_loja = df_merge_contoso.groupby('Nome_da_Loja')['Faturamento_Total'].sum()
Lucro_por_loja = df_merge_contoso.groupby('Nome_da_Loja')['Lucro_Total'].sum()

loja_top = vendas_por_loja.idxmax()
faturamento_top = vendas_por_loja.max()

loja_top_Lucro = Lucro_por_loja.idxmax()
top_Lucro = Lucro_por_loja.max()

print(f"A Loja com maior faturamento foi {loja_top} com R$ {faturamento_top:,.2f}")
print(f"A Loja com maior Lucro foi {loja_top_Lucro} com R$ {top_Lucro:,.2f}")


# In[124]:


#Qual Pais teve maior valor de faturamento e lucro??
#Qual loja vendeu mais em faturamento?
# Agrupar e somar faturamento
df_merge_contoso.rename(columns={'Nome da Loja': 'Nome_da_Loja'}, inplace=True)
vendas_por_Pais = df_merge_contoso.groupby('País')['Faturamento_Total'].sum()
Lucro_por_Pais = df_merge_contoso.groupby('País')['Lucro_Total'].sum()

pais_top = vendas_por_Pais.idxmax()
faturamento_top = vendas_por_Pais.max()

pais_top_Lucro = Lucro_por_Pais.idxmax()
top_Lucro = Lucro_por_Pais.max()

print(f"O Pais com maior faturamento foi {pais_top} com R$ {faturamento_top:,.2f}")
print(f"O Pais com maior Lucro foi {pais_top_Lucro} com R$ {top_Lucro:,.2f}")


# ## Principais Insights
# 
# 1. O mês com maior faturamento foi **novembro**, com $ 318.624.488,87.
# 
# 2. E o mês que teve a maior quantidade de peças vendidas **novembro** com 1,143,531
# 
# 5. A loja com maior faturamento foi **Loja Contoso Catalog**, com $ 277.058.181,11.
# 
# 6. A loja com maior lucro foi **Loja Contoso Catalog**, com $ 160.460.918,27.
# 
# 7. país com maior faturamento foi **Estados Unidos**, com $ 1.930.946.918,69.
# 
# 8. O país com maior lucro foi **Estados Unidos**, com $ 1.116.661.706,08.
# 
# 

# In[ ]:




