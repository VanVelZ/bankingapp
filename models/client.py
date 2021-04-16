from uuid import UUID
class Client:
    def __init__(self, name, id=0, accounts=None):
        if accounts is None:
            self.accounts = []
        else:
            self.accounts = accounts
        self.id = id
        self.name = name

    def __str__(self):
        return f"{self.name}: {self.accounts}"

    def __repr__(self):
        return str(self)

