from InquirerPy import prompt
from sisbanco import Conta, Banco
from modulo_prompt import perguntas, pegar_opcao

banco = Banco()

conta1 = Conta('1037-01')
conta2 = Conta('1057-02')

def terminal():
    sisbanco = Banco()
    opcoes = perguntas()

    while True:
        resposta = prompt(opcoes)
        opcao_str = list(resposta.values())[0]

        opcao = pegar_opcao(opcao_str)
        match opcao:

            case 0:
                numero = input('Digite o número da conta: ')
                conta = Conta(numero)
                sisbanco.cadastrar(conta)

            case 1:
                numero = input('Digite o número da conta: ')
                valor = float(input('Valor a ser creditado: '))
                sisbanco.creditar(numero, valor)
            case 2:
                numero = input('Digite o número da conta: ')
                valor = float(input('Valor a ser debitado: '))
                sisbanco.debitar(numero, valor)

            case 3:
                numero_origem = input('Digite o número da conta de origem: ')
                numero_destino = input('Digite o número da conta de destino: ')
                valor = float(input('Valor a ser transferido: '))
                sisbanco.transferir(numero_origem, numero_destino, valor)
            
            case 4:
                numero = input('Digite o número da conta: ')
                saldo = sisbanco.saldo(numero)
                print(saldo)
            
            case 5:
                print('SysBanco:: Bye!')
                return


if __name__ == '__main__':
    terminal()

