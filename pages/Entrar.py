import streamlit as st 

st.set_page_config(
    page_title="Entrar"
)


st.header("Entrar")
usuario = st.text_input("Usuário")
senha = st.text_input("Sua senha", type='password')
entrar = st.button("Entrar")
