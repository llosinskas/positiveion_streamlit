import numpy as np

class MV():
    
    def __init__(
            self,
            modelo,
            fabricante,
            comprimento,
            largura, 
            altura,
            tensao_oc, 
            corrente_sc, 
            tensao_pico, 
            corrente_pico,
            preco_unitario, 
            ter_corrente,
            ter_tensao, 
            ter_potencia, 
            ter_NOCT):
        
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

        # Dados elétricos STC
        self.potencia_pico
        self.tolerancia_potencia
        self.tensao_max_potencia
        self.corrente_max_potencia
        self.tensao_circuito_aberto
        self.corrente_curto_circuito 
        self.eficiencia
        
        # Dados elétricos NOCT
        self.potencia_max_noct
        self.tensao_max_potencia_noct
        self.corrente_max_potenca_noct
        self.tensao_circuito_aberto_noct
        self.curto_circuito_noct

        # Dados mecânicos 
        # Coeficiênte de temperatura 
        # Limites de operação
        # Garantia 