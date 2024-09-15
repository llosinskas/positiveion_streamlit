import io 

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from sankeyflow import Sankey

st.set_page_config(
    layout="wide", 
    page_title="Análises"
)
st.title("Análises energética de meus veículos")

st.sidebar.title("Configurações")
uploaded_file = st.sidebar.file_uploader("Adicionar dados externor CSV", type="csv")
if uploaded_file is not None:
    st.session_state.df = pd.read_csv(uploaded_file)


st.sidebar.number_input("Número de rotas", 5, 20, 10, 1, key="n_rota")
st.sidebar.selectbox(
    "Veículos",
    index=0,
    options=["Veiculo 1", "Veiculo 2", "Veiculo 3", "Veiculo 4"],
    key="veiculo",
)
st.sidebar.markdown("---")  # Horizontal line
st.sidebar.markdown("**[Manual](https://google.com/)**")

