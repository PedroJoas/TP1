from calc_v2 import Calculadora

numero1, numero2 = 11,5

calculadora = Calculadora()
soma = calculadora.soma(operando_a=numero1, operando_b=numero2)
sub = calculadora.subtracao(operando_a=numero1, operando_b=numero2)
mult = calculadora.multiplicacao(operando_a=numero1, operando_b=numero2)
div = calculadora.divisao(operando_a=numero1, operando_b=numero2)
acumulador = calculadora.retorne_acumulador()

print(f'Soma: {soma}')
print(f'{acumulador}')
print(f'Subtração: {sub}')
print(f'Multiplicação: {mult}')
print(f'Divisão: {div}')
print(f'{acumulador}')
