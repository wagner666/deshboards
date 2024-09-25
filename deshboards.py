import streamlit as st # Biblioteca para construir os deshbords
import pandas as pd  # Biblioteca de manipulação de dados  em python pra ler arquivos pra pode tratar
import plotly.express as px # Biblioteca para construir os graficos 


""" Pra cria o Deshboards tem que entra no terminal coloca o (streamlit run deshboards.py ou nome da pasta e clik enter e vai pedi pra bota o email e coloca e da enter que vai abrir) """


st.set_page_config(layout="wide") # Almenta a tabela do espaço horiontal 

# Com uma visão mensal
#faturamento por unidade...
#tipo de produto mais vendidos, contribuição por filial...
#desempenho das formas de pagamento...
#cocmo estão as avaliações das filias...

df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",") # importa o csv

df["Date"] = pd.to_datetime(df["Date"]) # ordenar

df=df.sort_values("Date") # ordenar

# Coloca pra ordenar em mes e ano
df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))

month = st.sidebar.selectbox("Mês", df["Month"].unique()) # criando uma caixa pra melhor identifica por data a tabela


df_filtered = df[df["Month"] == month]


# criando colunas
col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

# cria frafico que vai mes mostra o faturamento dia filtrado por mês
fig_date = px.bar(df_filtered, x="Date", y="Total", color = "City", title="Faturamento por dia")
col1.plotly_chart(fig_date, use_conteiner_width=True) # colocando a grafico na coluna 1

fig_prod = px.bar(df_filtered, x="Date", y="Product line",color="City", title="Faturamento por tipo de produto",orientation="h")
col2.plotly_chart(fig_prod, use_conteiner_width=True) # colocando a grafico na coluna 2




city_total = df_filtered.groupby("City") [["Total"]].sum().reset_index() # agrupar e selecionar e somar por cidados

fig_city = px.bar(city_total, x="City", y="Total", title="Faturamento por filial")
col3.plotly_chart(fig_city, use_conteiner_width=True) # colocando a grafico na coluna 3



fig_kind = px.pie(df_filtered, values="Total", names="Payment", title="Faturamento por tipo de pagamento")
col4.plotly_chart(fig_kind, use_conteiner_width=True) # colocando a grafico na coluna 4



city_total = df_filtered.groupby("City") [["Rating"]].mean().reset_index() # avaliação media por cidade
fig_rating = px.bar(df_filtered, y="Rating", x="City", title="Avaliação")
col5.plotly_chart(fig_rating, use_conteiner_width=True) # colocando a grafico na coluna 5
