from sisbanco import Banco, ContaEspecial, ContaPoupanca, ContaImposto, Conta
import unittest

class TestConta(unittest.TestCase):

    def test_creditar(self):
        conta = Conta('1234-X')
        conta.creditar(10)
        self.assertEqual(conta.get_saldo(), 10, 'Erro ao creditar')
    
    def test_debitar(self):
        conta = Conta('1234-X')
        conta.creditar(10)
        conta.debitar(10)
        self.assertEqual(conta.get_saldo(), 0, 'Erro ao debitar')

class TestContaPoupanca(unittest.TestCase):

    def test_render_juros(self):
        conta = ContaPoupanca('1234-X')
        conta.creditar(10)
        conta.render_juros(0.1)
        self.assertEqual(conta.get_saldo(), 11, 'Erro ao render juros')

class TestContaEspecial(unittest.TestCase):

    def test_creditar_especial(self):
        conta = ContaEspecial('1234-X')
        conta.creditar(10)
        self.assertEqual(conta.get_saldo(), 10, 'Erro ao creditar na conta especial')

    def test_render_bonus(self):
        conta = ContaEspecial('1234-X')
        conta.creditar(100)
        conta.render_bonus()
        self.assertEqual(conta.get_saldo(), 101, 'Erro ao render bonus')

class TestContaImposto(unittest.TestCase):

    def test_debitar(self):
        conta = ContaImposto('1234-X')
        conta.creditar(10000)
        conta.debitar(1000)
        self.assertTrue(conta.get_saldo() == 8999, 'Erro ao debitar conta imposto')

class TestBanco(unittest.TestCase):

    def test_cadastrar(self):
        banco = Banco()
        conta = Conta('1234-X')

        banco.cadastrar(conta)
        conta.creditar(10)
        self.assertTrue(banco.saldo('1234-X') == 10)

    def test_procurar(self):
        banco = Banco()
        conta = Conta('1234-X')

        banco.cadastrar(conta)

        conta_procurada = banco.procurar('1234-X')

        self.assertIsNotNone(conta_procurada)

    def test_tranferir(self):
        banco = Banco()
        conta1 = Conta('1234-X')
        conta2 = Conta('1235-X')

        banco.cadastrar(conta1)
        banco.cadastrar(conta2)

        banco.transferir('1234-X', '1235-X', 100)

        self.assertTrue(conta1.get_saldo() == -100)
        self.assertTrue(conta2.get_saldo() == 100)

if __name__ == '__main__':
    unittest.main()