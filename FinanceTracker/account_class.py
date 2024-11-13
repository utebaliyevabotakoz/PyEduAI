class Account:
    def __init__(self):
        self.balance = 0
        self.transactions = []


    def add_trans (self, transaction_object):
        self.transactions.append(transaction_object)
        self.balance += transaction_object.amount