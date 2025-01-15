from sisbanco import *
from excecoes import *

def terminal():
   sisbanco = Banco()
   while(True):
      print("SisBanco::Bem-Vindo!")
      print(".::Opcoes::.")
      print("[0] Cadastrar Conta")
      print("[1] Creditar")
      print("[2] Debitar")
      print("[3] Transferir")
      print("[4] Consultar Saldo")
      print("[5] Render Juros")
      print("[6] Render Bonus")
      print("[7] Alterar Taxa_Juros")      
      print("[8] Alterar Taxa_Imposto")
      print("[9] Sair")
      opcao = int(input("Digite:"))
      
      if opcao == 0:
         
         #qual tipo de conta a ser criada: 
         tipo_conta = input('Qual tipo de conta a ser criada: ').upper()
         #S - Simples  | P - Poupanca | E - Especial | I - Imposto
         #solicite o numero da conta a ser criada
         numero = input('Digite o número da conta: ')
         #instancie uma conta do tipo selecionado com esse numero
         if tipo_conta == 'S':
            conta = Conta(numero)
         elif tipo_conta == 'P':
            conta = ContaPoupanca(numero)
         elif tipo_conta == 'E':
            conta = ContaEspecial(numero)
         elif tipo_conta == 'I':
            conta = ContaImposto(numero)
         else:
            print('Tipo de conta inesxistente')
         
         #cadastre a conta no sisbanco
         try:
            sisbanco.cadastrar(conta)
         except VIException as vie:
            print(vie.print_mensagem_erro())
         else:
            print('Operação de Cadastramento correto!')

      elif opcao == 1:
         
         #solicite o numero da conta alvo
         numero = input('Digite o número da conta: ')
         #solicite o valor a ser creditado
         valor = float(input('Digite o valor a ser creditado: '))
         #realize a operacao de credito no sisbanco
         try:
            sisbanco.creditar(numero, valor)
         except VIException as vie:
            print(vie.print_mensagem_erro())

         else:
            print('Valor creditado com sucesso!')

      elif opcao == 2:
         
         #solicite o numero da conta alvo
         numero = input('Digite o número da conta: ')

         #solicite o valor a ser debitado
         valor = float(input('Digite o valor a ser debitado: '))
         #realize a operacao de debito no sisbanco
         try:
            sisbanco.debitar(numero, valor)

         except VIException as vie:
            print(vie.print_mensagem_erro())
         except SIException as sie:
            print(sie.print_mensagem_erro())
         else:
            print('Débito feito com sucesso!')

      elif opcao == 3:
         
         #solicite o numero da conta origem
         conta_origem = input('Digite o número da conta de origem: ')
         #solicite o numero da conta destino
         conta_destino = input('Digite o número da conta de destino: ')
         #solicite o valor a ser transferido
         valor = float(input('Digite o valor a ser transferido: '))
         #realize a operacao de transferencia no sisbanco
         try:
            sisbanco.transferir(conta_origem, conta_destino, valor)
         except SIException as sie:
            print(sie.print_mensagem_erro())
         except VIException as vie:
            print(vie.print_mensagem_erro())
         else:
            print('Transferência feita com sucesso!')

      elif opcao == 4:
         
         #solicite o numero da conta alvo
         numero = input('Digite o número da conta: ')
         #realize a operacao de obtencao de saldo no sisbanco
         saldo = sisbanco.saldo(numero)
         #exiba o saldo na tela
         print(f'Saldo da conta {numero}: {saldo}')

      elif opcao == 5:
         #solicite o numero da conta alvo
         numero = input('Digite o número da conta: ')
         #realize a operacao correcao da poupanca no sisbanco
         try:
            sisbanco.render_juros(numero)
         except TJIException as tje:
            print(tje.print_mensagem_erro())
         else:
            print('Operação de render juros com sucesso!')
         

      elif opcao == 6:
         
         #solicite o numero da conta alvo
         numero = input('Digite o número da conta: ')
         #realize a operacao conversao/rendimento de bonus no sisbanco
         try:
            sisbanco.render_bonus(numero)
         except VIException as vie:
            print(vie.print_mensagem_erro())
         else:
            print('Operação de rendimento bônus feita com sucesso!')

      elif opcao == 7:
         
         #solicite a nova taxa de correcao da poupanca
         taxa_poupanca = input('Digite a nova taxa da poupança: ')
         #realize a operacao de alteracao da taxa no sisbanco
         try:
            sisbanco.set_taxa_poupanca(taxa_poupanca)
         except VIException as vie:
            print(vie.print_mensagem_erro())
         else:
            print('Operação de correção da taxa da poupança feita com sucesso!')

      elif opcao == 8:
         
         #solicite a nova taxa de imposto
         taxa_imposto = input('Digite a nova taxa do imposto: ')
         #realize a operacao de alteracao da taxa no sisbanco
         try:
            sisbanco.set_taxa_imposto(taxa_imposto)
         except VIException as vie:
            print(vie.print_mensagem_erro())
         else:
            print('Operação de correção da taxa do imposto feita com sucesso!')
         
      elif opcao == 9:
         print("SisBanco::Bye!")
         break

      print('---'*20)
if __name__ == "__main__":
   terminal()