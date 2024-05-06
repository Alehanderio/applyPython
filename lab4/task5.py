class Transaction:
    def process(self):
        pass

class Transfer(Transaction):
    def __init__(self, from_account, to_account, amount):
        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount
    
    def process(self):
        print(f"Переказ {self.amount} з {self.from_account} на {self.to_account}")

class Payment(Transaction):
    def __init__(self, account, amount):
        self.account = account
        self.amount = amount
    
    def process(self):
        print(f"Платіж {self.amount} з {self.account}")

class Statement(Transaction):
    def __init__(self, account):
        self.account = account
    
    def process(self):
        print(f"Виписка для {self.account}")

# Приклад використання
transactions = [
    Transfer("Рахунок 1", "Рахунок 2", 100),
    Payment("Рахунок 3", 50),
    Statement("Рахунок 4")
]

for transaction in transactions:
    transaction.process()
