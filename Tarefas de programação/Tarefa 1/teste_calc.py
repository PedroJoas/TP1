from calc import Calculadora

numero1, numero2 = 6,5

calculadora = Calculadora()
soma = calculadora.soma(numero1, numero2)
sub = calculadora.subtracao(numero1, numero2)
mult = calculadora.multiplicacao(numero1, numero2)
div = calculadora.divisao(numero1, numero2)

print(f'Soma: {soma}')
print(f'Subtração: {sub}')
print(f'Multiplicação: {mult}')
print(f'Divisão: {div}')
