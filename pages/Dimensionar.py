import streamlit as st 


st.header("Dimensionar veiculo")

st.selectbox("Selecione a rota", ("Rota 1", "Rota 2", "Rota 3"))
st.selectbox("Selecione o combustível de preferencia", ("Diesel", "Elétrico", "GNV", "Hidrogênio"))
st.selectbox("Selecione o tipo de veiculo", ("Carga", "Passageiro"))
st.selectbox("Selecione a categora do ônibus", ("Padron", "Articulado"))


st.button("Calcular")