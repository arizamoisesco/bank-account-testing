class BankAccount:

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
        return self.balance
    
    def get_balance(self):
        return self.balance
    
    def transfer(self, current_balance, amount_send, destination_account):
        
        if  current_balance >= amount_send:
            destination_account.deposit(amount_send)
            self.withdraw(amount_send)
        else:
            return "No se puede realizar la trasnferencia saldo insuficiente"
        
        return self.get_balance()