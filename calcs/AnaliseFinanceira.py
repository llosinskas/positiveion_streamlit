# import pandas as pd 
# import numpy as np 

class Analise():
    # C = Capital [R$]
    # N = Número de períodos [meses]
    # j = Juros simples decorridos n períodos 
    # J = Juros compostos decorridos n períodos 
    # r = Taxa percentual de juros 
    # i = Taxa unitária de juros (i=r/100)
    # P = Principal valor atual 
    # M = Montante de capitalização simples 
    # S = Montante de capitalização composta 
    # WACC = Custo médio ponderado de capital 
    # CAPM = Capital Asset Pricing Model
    # FC = Fluxo de caixa [R$]


    def Payback_simples(P, FC):
        # payback = tempo de retorno em meses
        payback = P/FC
        return payback

    def Payback_simples_caixa_variavel(P, FCs):
        soma = -P
        caixa = []
        for index, FC in enumerate(FCs):
            
            soma += FC
            caixa.append(soma)
            if soma>=0:
                index_virtual = index-1
                caixa_negativo = -caixa[index_virtual-1]
                payback_mes = (FCs[index_virtual-1]/caixa_negativo)
                payback = index_virtual + payback_mes
                return payback
        payback = -1
        return payback 
    
    def VPL(P, FCs, r):
        soma = 0
        caixa = []
        caixa_acumulada = -P
        caixa_total_acumulado = []
        for index, FC in enumerate(FCs):
            caixa_acumulada += FC/((1+r)**index)
            soma+=FC/((1+r)**index)
            caixa.append(soma)
            caixa_total_acumulado.append(caixa_acumulada)
            
        vpl = -P+soma 
        return vpl, caixa, caixa_total_acumulado

    def VF(FC, r, n):
        valor_futuro = FC*(1+r)**n
        return valor_futuro
        
    def Juros_simples(capital, taxa_juros, periodo):
        juros = capital*taxa_juros*periodo
        return juros
    def Juros_compostos(capital, taxa_juros, periodo):
        


Analise.VPL(100, [10,20,45, 20, 50, 100], 0.10)

Analise.Payback_simples_caixa_variavel(10, [1,1,2,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])