import streamlit as st 
import pandas as pd 
import numpy as np 

def consumo_carro(desempenho, distancia, numero_carros):
    energia = desempenho*distancia*numero_carros
    return energia 


st.header("Dimensionamento solar")
st.header("Adição de cargas")

with st.form("Adicionar carro elétrico"):
    st.text("Adicionar frotas de carros elétricos")
    n_carros = st.number_input("Número de carros")
    desempenho_carro  = st.number_input("Desempenho dos carros [km/kWh]")
    distancia_mensal = st.number_input("Distancia percorrida mensal [km]")
    st.form_submit_button("Adicionar carro")


energia_carros = consumo_carro(desempenho_carro, distancia_mensal, n_carros)
st.text(f"Consumo total da adição de carros na frota é de {energia_carros}kWh/mês")

st.header("Projeto de viabilidade")
st.text("VPL - Valor presente líquido")
st.text("TIR - Análise da taxa interna de retorno")
st.text("Payback simples")
st.text("Payback descontado")

calcular = st.button("Calcular")


def Valor_presente_liquido(F_c, N, I_r, T, I):
    # F_ac  = Fluxo acumulados [R$]
    # F_c   = Fluxo de caixa descontado que corresponde à diferença entre as receitas e despesas realizadas a cada preíodo considerado, [R$]
    # I_r   = Taxa interna de retorno ou taxa de desconto
    
    # N     = Número de períodos
    # I     = Investimento total [R$]
    # J     = Juros compostos decorridos n períodos 
    # i     = Taxa unitária de juros (i = r/100)
    # P     = Principal ou valor atual
    # M     = Montante de capitalização simples 
    # S     = Montante de capitalização composta 
    # WACC  = Custo médio ponderado de capital
    # CAPM  = Capital Asset Pricing Model

    F_ac = []
    soma=0
    fluxo_caixa = -I
    for i in range(N):
        soma += F_c/(1+I_r)**i
        fluxo_caixa+=soma
        F_ac.append(fluxo_caixa)

    return F_ac

a = Valor_presente_liquido(27600, 20, 1.08,12, 84540 )
st.table(a)
st.bar_chart(a)

def Payback_simples(I, FC):
    # payback = Tempo de retorno de investimento (mês)
    # I       = Investimento total (R$)
    # FC      = Fluxo de caixa (R$/mês)
    payback = I/FC
    return payback


# def payback_fluxo_variavel():


def Valor_futuro(VP, r, N):
    VF = VP(1+r)**N
    return VF

def Juros_simples(c, r, n):
    j = c*n*r
    return j 

