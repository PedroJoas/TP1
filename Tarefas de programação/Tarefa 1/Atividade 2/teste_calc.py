from modulo_calc_v2 import *

numero1, numero2 = 6,5
somar = soma(operando_a=numero1, operando_b=numero2)
subtrair = subtracao(operando_a=numero1, operando_b=numero2)
multiplicar = multiplicacao(operando_a=numero1, operando_b=numero2)
dividir = divisao(operando_b=numero2)

print(f'Soma: {somar}')
print(f'Subtração: {subtrair}')
print(f'Multiplicação: {multiplicar}')
print(f'Divisão: {dividir}')