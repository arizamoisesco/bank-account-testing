import unittest, os

from src.bank_account import BankAccount

class BankAccountTests(unittest.TestCase):

    #Queda pendiente una tarea
    #El método setup se ejecuta antes de cualquier prueba y se puede usar para centralizar el código repetido y compartido entre las funciones de prueba
    def setUp(self):
        self.account = BankAccount(balance=1000, log_file="transaction_log.txt")

    #Método que se ejecuta al finalizar las pruebas
    def tearDown(self):
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)
    
    def _count_lines(self, filename):
        with open(filename, "r") as f:
            return len(f.readlines())
        
    def _read_lines(self, filename, text_compare): 
        with open(filename, "r") as f:
            for line in f:
                if text_compare.strip() in line.strip():
                    return True
        return False

    def test_deposit(self):

        new_balance = self.account.deposit(500)
        self.assertEqual(new_balance, 1500, "El balance no es igual")
        #assert new_balance == 1500

    def test_withdraw(self):

        new_balance = self.account.withdraw(200)
        #assert new_balance == 800
        self.assertEqual(new_balance, 800, "El balance no es igual")

    def test_get_balance(self):

        self.assertEqual(self.account.get_balance(), 1000)
        #assert self.account.get_balance() == 1000

    def test_transfer(self):
        current_balance = self.account.get_balance()
        destination_account = BankAccount(balance=2000)
        amount_send = 500

        self.assertEqual(self.account.transfer(current_balance, amount_send, destination_account), 500)
        #assert self.account.transfer(current_balance, amount_send, destination_account) == 500
    
    def test_transfer_no_balance(self):
        current_balance = 0
        destination_account = BankAccount(balance=2000)
        amount_send = 500

        self.assertEqual(self.account.transfer(current_balance, amount_send, destination_account),"No se puede realizar la trasnferencia saldo insuficiente")
        #assert self.account.transfer(current_balance, amount_send, destination_account) == "No se puede realizar la trasnferencia saldo insuficiente"

    def test_trasnfer_log_no_balance(self):
        current_balance = 0
        destination_account = BankAccount(balance=2000)
        amount_send = 500
        self.account.transfer(current_balance, amount_send, destination_account)

        self.assertTrue(self._read_lines(self.account.log_file,"No tiene saldo disponible"))
        #assert self._read_lines(self.account.log_file,"No tiene saldo disponible") == True #Ya funciona

    def test_transaction_log(self):
        self.account.deposit(500)

        self.assertTrue(os.path.exists("transaction_log.txt"))
        #assert os.path.exists("transaction_log.txt")

    def test_count_transactions(self):
        self.assertEqual(self._count_lines(self.account.log_file), 1)
        #assert self._count_lines(self.account.log_file) == 1
        self.account.deposit(500)
        self.assertEqual(self._count_lines(self.account.log_file), 2)
        #assert self._count_lines(self.account.log_file) == 2