import unittest

from src.bank_account import BankAccount

class BankAccountTests(unittest.TestCase):

    #Queda pendiente una tarea
    #El método setup se ejecuta antes de cualquier prueba y se puede usar para centralizar el código repetido y compartido entre las funciones de prueba
    def setUp(self):
        self.account = BankAccount(balance=1000)

    def test_deposit(self):

        new_balance = self.account.deposit(500)
        assert new_balance == 1500

    def test_withdraw(self):

        new_balance = self.account.withdraw(200)
        assert new_balance == 800

    def test_get_balance(self):

        assert self.account.get_balance() == 1000

    def test_transfer(self):
        current_balance = self.account.get_balance()
        destination_account = BankAccount(balance=2000)
        amount_send = 500

        assert self.account.transfer(current_balance, amount_send, destination_account) == 500
    
    def test_transfer_no_balance(self):
        current_balance = 0
        destination_account = BankAccount(balance=2000)
        amount_send = 500

        assert self.account.transfer(current_balance, amount_send, destination_account) == "No se puede realizar la trasnferencia saldo insuficiente"