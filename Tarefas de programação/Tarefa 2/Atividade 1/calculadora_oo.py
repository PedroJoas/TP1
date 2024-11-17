class Calculadora:
    
    def __init__(self) -> None:
        pass

    def somar(self,operando_a,operando_b) -> float:
        return operando_a + operando_b
    
    def multiplicar(self,operando_a,operando_b) -> float:
        return operando_a * operando_b
    
    def subtrair(self,operando_a,operando_b) -> float:
        return operando_a - operando_b
    
    def dividir(self,operando_a,operando_b) -> float:
        if operando_a != 0:

            return operando_a / operando_b
        else:
            print('ERROR: Divisão por 0')
    

    
    
    
    