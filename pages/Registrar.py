import streamlit as st 

st.set_page_config(
    page_title="Registrar"
)


st.header("Registre")
nome = st.text_input("Nome")
email = st.text_input("E-mail")
usuario = st.text_input("Usuário")
senha = st.text_input("Sua senha", type='password')
senha1 = st.text_input("Digite novamente a sua senha", type='password')
entrar = st.button("Entrar")
