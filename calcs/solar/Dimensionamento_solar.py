import numpy as np
# import models.moduloFV as MV
# Dimensionamento solar 

class Inversor:
    def __init__(self,
                modelo,
                potencia, 
                tensao_maxima_cc, 
                tensao_minina_cc, 
                tensao_saida_ca,corrente_maxima_cc, 
                corrente_saida_ca, 
                potencia_pico, 
                frequencia, 
                eficiencia, 
                preco_unitario):
        self.modelo             = modelo
        self.potencia           = potencia
        self.tensao_maxima_cc   = tensao_maxima_cc
        self.tensao_minima_cc   = tensao_minina_cc
        self.tensao_saida_ca    = tensao_saida_ca
        self.corrente_maxima_cc = corrente_maxima_cc
        self.corrente_saida_ca  = corrente_saida_ca
        self.potencia_pico      = potencia_pico
        self.frequencia         = frequencia
        self.eficiencia         = eficiencia
        self.preco_unitário     = preco_unitario

class MV:
    def __init__(self,modelo, comprimento,largura, altura,tensao_oc, corrente_sc, tensao_pico, corrente_pico,preco_unitario, ter_corrente,ter_tensao, ter_potencia, ter_NOCT ):
        self.modelo         = modelo
        self.comprimento    = comprimento
        self.largura        = largura
        self.altura         = altura
        self.tensao_oc      = tensao_oc
        self.corrente_sc    = corrente_sc
        self.tensao_pico    = tensao_pico
        self.corrente_pico  = corrente_pico
        self.preco_unitario = preco_unitario
        self.ter_corrente   = ter_corrente
        self.ter_tensao     = ter_tensao
        self.ter_potencia   = ter_potencia
        self.ter_NOCT       = ter_NOCT

class Cidade:
    def __init__(self, pais, cidade, temp_maxima, temp_media, temp_minima):
        self.pais           = pais
        self.cidade         = cidade
        self.temp_maxima    = temp_maxima
        self.temp_media     = temp_media
        self.temp_minima    = temp_minima

class Dimensionamento_solar:
    def Dimensionamento_B(consumo, painel,inversor, cidade, tarifa, eficiencia_global, irradiacao, sobrecarregamento_cc):
        area_painel = painel.comprimento*painel.largura
        potencia_pico = int(painel.tensao_pico*painel.corrente_pico)
        media_consumo = np.mean(consumo)
        potencia_instalada = round(media_consumo*1000/(irradiacao*eficiencia_global*30),-1)
        n_painel = round(potencia_instalada/potencia_pico)
        potencia_total_MV = potencia_pico*n_painel/1000
        coeficiente_ajuste_temperatura = (painel.ter_NOCT-20)/800
        temp_operacao_maxima = cidade.temp_maxima+coeficiente_ajuste_temperatura*1000
        temp_operacao_minima = cidade.temp_minima + coeficiente_ajuste_temperatura*1000
        voc_T = painel.tensao_oc*(1+painel.ter_tensao*(temp_operacao_maxima-25))
        vp_T = painel.tensao_pico*(1+painel.ter_tensao*(temp_operacao_minima-25))
        area_total_painel = area_painel*n_painel
        n_max_string = round(inversor.tensao_maxima_cc/voc_T)
        n_min_string = round(inversor.tensao_minima_cc/vp_T)
        tensao_max_string = n_max_string*painel.tensao_pico
        tensao_min_string = n_min_string*painel.tensao_pico
        n_string = round(n_painel/n_min_string)
        n_painel_paralelo = 0
        if n_string==0:
            n_painel_paralelo=1
        else:
            n_painel_paralelo=n_painel/n_string

        tensao_arranjo = 0
        if n_painel_paralelo==0:
            tensao_arranjo = painel.tensao_pico*n_painel
        else:
            tensao_arranjo = n_painel_paralelo*painel.tensao_pico

        corrente_arranjo = 0

        if n_string == 1:
            corrente_arranjo = painel.corrente_pico
        else:
            corrente_arranjo = (n_painel/n_painel_paralelo)*painel.corrente_pico
        print("hello")
    # def Dimensionamento_A(consumo, painel, tarifa, eficiencia_global, irradiacao, sobrecarregamento_cc):
        

cidade = Cidade("Brasil", "São Paulo", 32, 24, 24)
inversor = Inversor("SMA Sunny 30000TL-21 INT", 10, 750, 175, 220, 30, 33, 10, 60, 0.97, 10490)
painel = MV("Atersa A-265P", 1.645, 0.99, 0.04, 38.14, 9.01, 31.55,8.4, 818, 0.0004, -0.0032,-0.0043,47)
Dimensionamento_solar.Dimensionamento_B(
    [1398,1398,1398,4000,1398,1398,1398,1398,1398,1398,1398,1398], 
    painel, 
    inversor, 
    cidade, 
    0.86, 
    0.8, 
    5.5, 
    1.2
    )

        