from InquirerPy import prompt
from sisbanco import Conta, Banco, ContaEspecial, ContaPoupanca
from modulo_prompt import perguntas, pegar_opcao

def terminal():
    sisbanco = Banco(taxa=0.01)
    opcoes = perguntas()

    while True:
        resposta = prompt(opcoes)
        opcao_str = list(resposta.values())[0]

        opcao = pegar_opcao(opcao_str)
        match opcao:

            case 0:
                tipo_conta = input('Qual tipo de conta a ser criada: ')
                numero = input('Digite o número da conta: ')

                if tipo_conta == 'S':
                    conta = Conta(numero)

                elif tipo_conta == 'P':
                    conta = ContaPoupanca(numero)

                elif tipo_conta == 'E':
                    conta = ContaEspecial(numero)

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
                numero = input('Digite o número da conta: ')
                sisbanco.render_juros(numero)

            case 6:
                numero = input('Digite o número da conta de origem: ')
                sisbanco.render_bonus(numero)
            
            case 7:

                taxa = float(input('Digite a nova taxa: '))
                sisbanco.set_taxa_poupanca(taxa)

            case 8:
                taxa = float(input('Digite a nova taxa: '))
                sisbanco.set_taxa_imposto(taxa)

            case 9:
                print('SysBanco:: Bye!')
                return


if __name__ == '__main__':
    terminal()

