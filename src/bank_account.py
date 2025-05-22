from datetime import datetime
from src.exceptions import WithdrawalTimeRestrictionError, WithdrawalDayRestrictionError

class BankAccount:

    def __init__(self, balance=0, log_file=None):
        self.balance = balance
        self.log_file = log_file
        self._log_transaction('Cuenta creada')

    def _log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(f"{message}\n")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._log_transaction(f"Deposited {amount}. New balance: {self.balance}")
        return self.balance
    
    def withdraw(self, amount):

        now = datetime.now()

        if now.hour < 8 or now.hour > 17:
            raise WithdrawalTimeRestrictionError("Withdrawal are only allowed from 8 am to 5 pm")
        
        if now.weekday() > 4:
            raise WithdrawalDayRestrictionError("Withdrawal are only allowed laboral Week ")

        if amount > 0:
            self.balance -= amount
            self._log_transaction(f"Withdrew {amount}. New balance: {self.balance}")
        return self.balance
    
    def get_balance(self):
        self._log_transaction(f"Checked balance. Current balance: {self.balance}")
        return self.balance
    
    def transfer(self, current_balance, amount_send, destination_account):#este código se puede mejorar con un try
        
        if  current_balance >= amount_send:
            destination_account.deposit(amount_send)
            self.withdraw(amount_send)
        else:
            self._log_transaction(f"No tiene saldo disponible")
            return "No se puede realizar la trasnferencia saldo insuficiente"
        
        return self.get_balance()