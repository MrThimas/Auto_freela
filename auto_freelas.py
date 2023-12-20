import os
import pandas as pd 
import streamlit as st 
import plotly.express as px 


st.title("Automação de Planilhas")
caminho = "Vendas/"
planilhas = os.listdir(caminho)

tabela_consolidada = pd.DataFrame()

for nome_planilha in planilhas:
    vendas_planilhas = pd.read_excel(os.path.join(caminho, nome_planilha))
    vendas_planilhas = vendas_planilhas.sort_values(by = "Data da Venda")
    tabela_consolidada = pd.concat([tabela_consolidada, vendas_planilhas])


col1, col2= st.columns(2)

fig_vendas = px.bar(tabela_consolidada, x="Data da Venda", y="Qtd Vendida", color="ID Loja")
col1.plotly_chart(fig_vendas)
tabela_consolidada.to_excel("Vendas total.xlsx")