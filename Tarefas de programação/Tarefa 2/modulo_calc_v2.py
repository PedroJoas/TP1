acumulador = 0


def soma(operando_b: float, operando_a: float = None ) -> float:
    global acumulador
    if operando_a != None:
        soma = operando_a + operando_b
        acumulador = soma
    else:
        soma = acumulador + operando_b
    return soma

def subtracao(operando_b: float, operando_a: float = None ) -> float:
    global acumulador
    if operando_a != None:
        sub = operando_a - operando_b
        acumulador = sub
    else:
        sub = acumulador - operando_b
    return sub
    
def multiplicacao(operando_b: float, operando_a: float = None) -> float:
        global acumulador
        if operando_a != None:
            mult = operando_a * operando_b
            acumulador = mult
        else:

            mult = acumulador * operando_b
        return mult
    
def divisao(operando_b: float, operando_a: float = None) -> float:
        global acumulador
        if operando_a != None:
            div = operando_a / operando_b
            acumulador = div
        else:
            div = acumulador / operando_b

        return div
