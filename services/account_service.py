from daos.accounts_dao import AccountsDAO


class AccountService:

    @staticmethod
    def create_account(account):
        return AccountsDAO.create_account(account)

    @staticmethod
    def get_all_accounts():
        return AccountsDAO.get_all_accounts()

    @staticmethod
    def get_account(client_id, account_id):
        return AccountsDAO.get_account(client_id, account_id).serialize()

    @staticmethod
    def get_account_by_client(id):
        accounts = []
        for account in AccountsDAO.get_accounts_by_client(id):
            accounts.append(account.serialize())
        return accounts

    @staticmethod
    def delete_account(id):
        return AccountsDAO.delete_account(id)

    @staticmethod
    def update_account(account):
        return AccountsDAO.update_account(account)
