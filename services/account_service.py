from daos.accounts_dao import AccountsDAO


class AccountService:

    @staticmethod
    def create_account():
        pass

    @staticmethod
    def get_all_accounts():
        pass

    @staticmethod
    def get_account(id):
        pass

    @staticmethod
    def get_account_by_client(id):
        return AccountsDAO.get_accounts_by_client(id)

    @staticmethod
    def delete_account(id):
        pass

    @staticmethod
    def update_account(account):
        pass

    @staticmethod
    def withdraw(account, amount):
        pass

    @staticmethod
    def deposit(account, amount):
        pass