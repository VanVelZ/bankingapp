from daos.accounts_dao import AccountsDAO


class AccountService:

    @staticmethod
    def create_account(account):
        return AccountsDAO.create_account(account)

    @staticmethod
    def get_all_accounts():
        return AccountsDAO.get_all_accounts()

    @staticmethod
    def get_account(id):
        return AccountsDAO.get_account(id)

    @staticmethod
    def get_account_by_client(id):
        return AccountsDAO.get_accounts_by_client(id)

    @staticmethod
    def delete_account(id):
        return AccountsDAO.delete_account(id)

    @staticmethod
    def update_account(account):
        return AccountsDAO.update_account(account)
