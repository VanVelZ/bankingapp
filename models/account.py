import uuid


class Account:

    def __init__(self, account_type, id=0, balance=0):
        self.account_type = account_type
        self.balance = balance
        self.id = id

    def __str__(self):
        return f"{self.account_type}: {self.balance}"

    def __repr__(self):
        return str(self)
