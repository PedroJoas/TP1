def decorator(func):
    def wrapper(x: float, y: float):
        print(f'Dividendo: {x}/{y}')
        if y == 0:
            return "ERRO_DIV_POR_ZERO"
        
        return func(x, y)
    return wrapper

@decorator
def dividir(operando_a: float, operando_b: float):
    return operando_a/operando_b


if __name__ == '__main__':
    print(f'-> Resultado:  {dividir(3,3)}\n')

    print(f'-> Resultado:  {dividir(3,0)}')

