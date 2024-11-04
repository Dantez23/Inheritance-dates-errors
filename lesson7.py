class account:
    def __init__(self, full_name, account_number,phone, balance): # method/function constructor --> set up info
        self.name = full_name
        self.number = account_number
        self.phone = phone
        self.balance = balance

def deposit(self, amount):
    self.balance += amount
    print(f"Amount ${amount} deposited successfully to account ${self.account.number}")

def withdraw(self, amount):
    if self.balance < amount:
        print(f"insufficient funds. Balance is ${self.balance}")
    else:
        self.balance -= amount
        print(f"Amount ${amount} withdrawn successfully from account ${self.account.number}")

def check_balance(self):
    print(f"Balance for account ${self.account_number} is: ${self.balance}")

kevo_acc = Account("Kevin Maina","0001","0712345678", 10000)
sara_acc = Account("Sara", "0002", "0712645688", "1800")
kevo_acc.deposit(2000)
kevo_acc.check_balance()
