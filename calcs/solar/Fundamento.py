# Classe para desenvolvimento dos fundamentos da energia solar
# @autor: Lucas Losinskas 
# data:09/2024
# 
# 

import numpy as np
class Solar:


    def Dia_ano(dia, mes):
        #calculo da cor
        if mes<=2:
            cor=int(mes/2)
        elif mes<=8:
            cor = int(mes/2-2)
        else:
            cor = int(mes/2+0.5)-2
        
        n = dia+(mes-1)*30+cor  
        return n 
    
    def declinacao_solar(n):
        declinacao = 23.45*np.sin(np.radians(360/365*(284+n)))
        return declinacao

    def Hora_solar(n, l0,l, HL):

        B = np.radians(360/364*(n-81))
        E = 9.87*np.sin(2*B) - 7.53*np.cos(B)-1.5*np.sin(B)
        corhora = (4*(l0-l)+E)/60
        HS = HL+corhora
        return HS

    def Angulo_horario(HS):
        omega = (HS-12)*15
        return omega

n = Solar.Dia_ano(25,10)
declinacao = Solar.declinacao_solar(n)
HS = Solar.Hora_solar(n, 45,46.73,14.5)
omega = Solar.Angulo_horario(HS)
print("helo")E-mail