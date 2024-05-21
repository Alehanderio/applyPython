class Transaction:
    def process(self):
        pass

class Transfer(Transaction):
    def __init__(self, from_account, to_account, amount):
        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount
    
    def process(self):
        print(f"Transfer {self.amount} $ from {self.from_account} to {self.to_account}")

class Payment(Transaction):
    def __init__(self, account, amount):
        self.account = account
        self.amount = amount
    
    def process(self):
        print(f"Payment {self.amount} from {self.account}")

class Statement(Transaction):
    def __init__(self, account):
        self.account = account
    
    def process(self):
        print(f"Statement for {self.account}")

# example 
transactions = [
    Transfer("123456", "654321", 100),
    Payment("111223", 50),
    Statement("432221")
]

for transaction in transactions:
    transaction.process()
