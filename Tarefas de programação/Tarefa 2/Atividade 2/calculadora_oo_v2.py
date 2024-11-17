class Calculadora:

    def __init__(self) -> None:
        self.acumulador = 0

    def soma(self, operando_a: float, operando_b: float = None ) -> float:
        if operando_b != None:
            soma = operando_a + operando_b
            self.acumulador = soma
        else:
            soma = self.acumulador + operando_a
        return soma

    def subtracao(self, operando_a: float, operando_b: float = None ) -> float:
        if operando_b != None:
            sub = operando_a - operando_b
            self.acumulador = sub
        else:
            sub = self.acumulador - operando_a
        return sub
    
    def multiplicacao(self, operando_a: float, operando_b: float = None) -> float:
        if operando_b != None:
            mult = operando_a * operando_b
            self.acumulador = mult
        else:

            mult = self.acumulador * operando_a
        return mult
    
    def divisao(self, operando_a: float, operando_b: float = None) -> float:
        if operando_b != None:
            div = operando_a / operando_b
            self.acumulador = div
        else:
            div = self.acumulador / operando_a

        return div
    
    def retorne_acumulador(self):
        return self.acumulador
    