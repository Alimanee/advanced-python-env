class BankAccount:
    def __init__(self, owner, balance=0):
        self._owner = owner
        self._balance = balance 
    def deposit(self, value):
        if value > 0:
            self._balance += value
            print(f"Deposited: {value}")
        else:
            print("Deposit amount must be positive")
    def withdraw(self, value):
        if value < 0:
            print("Withdrawal amount must be positive")
        elif value > self._balance:
            print("Insufficient balance")
        else:
            self._balance -= value
            print(f"Withdraw: {value}")
    def balance(self):
        return self._balance
account = BankAccount("Alisher", 10000)
account.deposit(1500)
account.withdraw(500)
account.withdraw(6000)
account.deposit(-450)
print(f"Current balance: {account.balance()}")