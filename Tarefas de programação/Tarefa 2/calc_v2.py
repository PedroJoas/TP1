class Calculadora:

    def __init__(self) -> None:
        self.acumulador = 0

    def soma(self, operando_b: float, operando_a: float = None ) -> float:
        if operando_a != None:
            soma = operando_a + operando_b
            self.acumulador = soma
        else:
            soma = self.acumulador + operando_b
        return soma

    def subtracao(self, operando_b: float, operando_a: float = None ) -> float:
        if operando_a != None:
            sub = operando_a - operando_b
            self.acumulador = sub
        else:
            sub = self.acumulador - operando_b
        return sub
    
    def multiplicacao(self, operando_b: float, operando_a: float = None) -> float:
        if operando_a != None:
            mult = operando_a * operando_b
            self.acumulador = mult
        else:

            mult = self.acumulador * operando_b
        return mult
    
    def divisao(self, operando_b: float, operando_a: float = None) -> float:
        if operando_a != None:
            div = operando_a / operando_b
            self.acumulador = div
        else:
            div = self.acumulador / operando_b

        return div
    
    def retorne_acumulador(self):
        return self.acumulador
    