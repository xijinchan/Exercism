import threading

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.active = False
        self.mutex = threading.Lock()

    def get_balance(self):
        if self.active == False: raise ValueError('account not open') 
        return self.balance

    def open(self):
        if self.active == True: raise ValueError('account already open')
        self.active = True
        self.balance = 0

    def deposit(self, amount):
        if self.active == False: raise ValueError('account not open') 
        if amount <= 0: raise ValueError('amount must be greater than 0')

        with self.mutex: self.balance += amount

    def withdraw(self, amount):
        if self.active == False: raise ValueError('account not open') 
        if amount <= 0: raise ValueError('amount must be greater than 0')
        if amount > self.balance: raise ValueError('amount must be less than balance')
        
        with self.mutex: self.balance -= amount

    def close(self):
        if self.active == False: raise ValueError('account not open') 
        self.active = False
