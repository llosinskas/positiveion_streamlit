import streamlit as st 
import pandas as pd

st.set_page_config(
    page_title="Notificações", 
    layout='wide'
)
st.header("Notificações")

df = pd.DataFrame([["Descrição", "data"], ["Veiculo qubrou rolamento", "22/2/2023"], ["Manutenção Preventiva veículo 3151", "20/4/2024"]])

df

