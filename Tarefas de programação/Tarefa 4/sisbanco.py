from abc import ABC, abstractmethod

# CLASSE CONTA ABSTRATA
def ContaAbstrata(ABC):

    def __init__(self, numero: str) -> None:
        pass
    
    def creditar(self, valor):
        self.__saldo += valor

    @abstractmethod
    def debitar(self, valor) -> None:
        pass
    
    def get_numero(self):
        return self.__numero
    
    def get_saldo(self):
        return self.__saldo

# CLASSE CONTA
class Conta(ContaAbstrata):

    def __init__(self, numero):
        self.__numero = numero
        self.__saldo = 0

    def creditar(self, valor):
        self.__saldo += valor

    def debitar(self, valor):
        self.__saldo -= valor
    
    def get_numero(self):
        return self.__numero
    
    def get_saldo(self):
        return self.__saldo
    
# CLASSE CONTA POUPANÇA
class ContaPoupanca(Conta):

    def __init__(self, numero: str):
        super().__init__(numero)
    
    def render_juros(self, taxa: float) -> None:
        self.creditar(self.get_saldo() * taxa)
    
# CLASSE CONTA ESPECIAL
class ContaEspecial(Conta):

    def __init__(self, numero):
        super().__init__(numero)
        self.__bonus = 0
    
    def render_bonus(self) -> None:
        super().creditar(self.__bonus)
    
    def creditar(self, valor: float) -> None:
        self.__bonus += valor * 0.01
        super().creditar(valor)

# CLASSE CONTA IMPOSTO
class ContaImposto(ContaAbstrata):

    def __init__(self, numero):
        super().__init__(numero)
        self.__taxa = 0.001
    
    def debitar(self, valor: float) -> None:
        self.__saldo = self.__saldo - (valor + (valor * self.__taxa))
    
    def get_taxa(self) -> float:
        return self.__saldo

    def set_taxa(self, taxa: float) -> None:
        self.__taxa = taxa
    

class Banco:
    
    def __init__(self, taxa_poupanca:float = 0.001, taxa_imposto: float = 0.001) -> None:
        self.__taxa_poupanca = taxa_poupanca
        self.__taxa_imposto = taxa_imposto
        self.__contas = []
        pass

    def cadastrar(self, conta: Conta) -> None:
        self.__contas.append(conta)
    
    def procurar(self, numero:str) -> Conta:
        for conta in self.__contas:
            if numero == conta.get_numero():
                return conta
        return None
    
    def creditar(self, numero:str, valor:float) -> None:
        conta = self.procurar(numero)

        if conta is not None:
            conta.creditar(valor)
    
    def debitar(self, numero:str, valor:float) -> None:
        conta = self.procurar(numero)

        if conta is not None:
            if isinstance(conta, ContaImposto):
                conta.set_taxa(self.__taxa_imposto)
            
            conta.debitar(valor)


    def saldo(self, numero:str) -> float:
        conta = self.procurar(numero)

        if conta is not None:
            return conta.get_saldo()
    
    def transferir(self, origem:str, destino:str,  valor:float) -> None:
        conta_origem = self.procurar(origem)
        conta_destino = self.procurar(destino)

        if conta_origem is not None and conta_destino is not None:
            conta_origem.debitar(valor)
            conta_destino.creditar(valor)
    
    def render_juros(self, numero:str) -> None:
        conta = self.procurar(numero)

        if (conta is not None) and (isinstance(conta, ContaPoupanca)):
            conta.render_juros(self.__taxa)
    
    def get_taxa_poupanca(self) -> float:
        return self.__taxa_poupanca

    def set_taxa_poupanca(self, taxa) -> None:
        self.__taxa_poupanca = taxa

    def render_bonus(self, numero: str) -> None:
        conta = self.procurar(numero)

        if (conta is not None) and (isinstance(conta, ContaEspecial)):
            conta.render_bonus()
    
    def get_taxa_imposto(self) -> float:
        return self.__taxa_imposto

    def set_taxa_imposto(self, taxa) -> None:
        self.__taxa_imposto = taxa
