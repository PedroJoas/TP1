import re
def perguntas():
    opcoes = [
        {
            'type':'list',
            'message':'SisBanco : : Bem−Vindo! \n ---- Opçoes -----',
            'choices': ["[0] − CriarConta", "[1] − Creditar", "[2] − Debitar", 
                        "[3] − Transferir", "[4] − Saldo", "[5] − Render juros", 
                        "[6] − Render Bônus", "[7] − Alterar taxa de juros", "[8] − Alterar Taxa Imposto",
                        "[9] - Sair"]
        }
    ]
    return opcoes

def pegar_opcao(string_opcao):
    match = re.search(r'\[(\d+)\]', string_opcao)

    if match:
        numero = int(match.group(1))
        return numero
    else:
        print('Nenhum número encontrado entre colchetes.')
