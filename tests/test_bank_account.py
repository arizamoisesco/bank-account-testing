import unittest, os

from unittest.mock import patch

from src.exceptions import WithdrawalTimeRestrictionError, WithdrawalDayRestrictionError

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

    def test_deposit_positive_amount_increase_balance(self):

        new_balance = self.account.deposit(500)
        self.assertEqual(new_balance, 1500, "El balance no es igual")
        #assert new_balance == 1500

    def test_withdraw_negative_amount_decrease_balance(self):

        new_balance = self.account.withdraw(200)
        #assert new_balance == 800
        self.assertEqual(new_balance, 800, "El balance no es igual")

    def test_get_balance_returns_current_balance(self):

        self.assertEqual(self.account.get_balance(), 1000)
        #assert self.account.get_balance() == 1000

    def test_transfer_amount_send_decrease_balance(self):
        current_balance = self.account.get_balance()
        destination_account = BankAccount(balance=2000)
        amount_send = 500

        self.assertEqual(self.account.transfer(current_balance, amount_send, destination_account), 500)
        #assert self.account.transfer(current_balance, amount_send, destination_account) == 500
    
    def test_transfer_no_balance_amount_send_deny_transfer(self):
        current_balance = 0
        destination_account = BankAccount(balance=2000)
        amount_send = 500

        self.assertEqual(self.account.transfer(current_balance, amount_send, destination_account),"No se puede realizar la trasnferencia saldo insuficiente")
        #assert self.account.transfer(current_balance, amount_send, destination_account) == "No se puede realizar la trasnferencia saldo insuficiente"

    def test_trasnfer_amount_send_log_no_balance(self):
        current_balance = 0
        destination_account = BankAccount(balance=2000)
        amount_send = 500
        self.account.transfer(current_balance, amount_send, destination_account)

        self.assertTrue(self._read_lines(self.account.log_file,"No tiene saldo disponible"))
        #assert self._read_lines(self.account.log_file,"No tiene saldo disponible") == True #Ya funciona

    def test_transaction_log_positive_amount_create_log(self):
        self.account.deposit(500)

        self.assertTrue(os.path.exists("transaction_log.txt"))
        #assert os.path.exists("transaction_log.txt")

    def test_count_transactions_new_deposit_total_transactions(self):
        self.assertEqual(self._count_lines(self.account.log_file), 1)
        #assert self._count_lines(self.account.log_file) == 1
        self.account.deposit(500)
        self.assertEqual(self._count_lines(self.account.log_file), 2)
        #assert self._count_lines(self.account.log_file) == 2

    @patch("src.bank_account.datetime") #Accedemos al módulo de
    def test_withdraw_during_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10 #Validando que funcione si el horario es a las 10 am
        new_balance = self.account.withdraw(100)
        self.assertEqual(new_balance, 900)


    @patch("src.bank_account.datetime") #Accedemos al módulo de
    def test_withdraw_disallow_before_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 7 #Validando que falle si el horario es a las 7 am
        with self.assertRaises(WithdrawalTimeRestrictionError):

            self.account.withdraw(100)

    @patch("src.bank_account.datetime") #Accedemos al módulo de
    def test_withdraw_disallow_after_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 5 #Validando que falle si el horario es a las 7 am
        with self.assertRaises(WithdrawalTimeRestrictionError):

            self.account.withdraw(100)

    @patch("src.bank_account.datetime")
    def test_withdraw_disallow_weekends(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10 # Hay que poner la hora valida 
        mock_datetime.now.return_value.weekday.return_value = 5 # Ahora si poner lo necesario para que falle en los dias correspondientes
        with self.assertRaises(WithdrawalDayRestrictionError):

            self.account.withdraw(100)

    def test_deposit_multiple_ammounts(self):
        test_cases = [
            {"ammount": 100, "expected":1100},
            {"ammount": 3000, "expected":4000},
            {"ammount": 4500, "expected":5500},
        ]
        for case in test_cases:
            with self.subTest(case=case):
                self.account = BankAccount(balance=1000, log_file="transactions.txt")
                new_balance = self.account.deposit(case["ammount"])
                self.assertEqual(new_balance, case["expected"])