import streamlit as st 
from streamlit_elements import elements, mui, html
import numpy as np
import pandas as pd
st.set_page_config(
    layout="wide", 
    page_title="Meus Veiculos"
)

# Sidebar
@st.experimental_dialog("Adicionar Veiculo")
def adicionar_veiculo():
        modelo = st.text_input("Modelo")
        fabricante = st.text_input("fabricante")
        peso = st.number_input("Peso [ton]")
        ano_fabricacao = st.date_input("Ano de fabricação")
        data = st.date_input("Data da aquisição")
        categoria = st.selectbox("Categoria", ("Veiculo de carga", "Passageiro", "Particular"))

add_veiculo = st.sidebar.button("Adicionar veiculo")
if add_veiculo:
     adicionar_veiculo()

# Body 
st.header("Meus Veiculos")
df = pd.DataFrame(
np.random.randn(4, 2) / [50, 50] + [-22, -46],
columns=['lat', 'lon'])
map = st.map(df)


df2 = pd.DataFrame([["Modelo", "Fabricante", "Número"], ["Volvo","Volvo", "1010"], ["Mercedes","5410", "1011"], ["Volvo","Volvo", "1010"]])
df2