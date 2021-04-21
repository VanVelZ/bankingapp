from daos.accounts_dao import AccountsDAO


class AccountService:

    @staticmethod
    def create_account(account, client_id):
        return AccountsDAO.create_account(account, client_id)

    @staticmethod
    def get_all_accounts():
        return AccountsDAO.get_all_accounts()

    @staticmethod
    def get_account(client_id, account_id):
        account = AccountsDAO.get_account(client_id, account_id)
        return account.serialize() if account else ("Account/Client not found", 404)

    @staticmethod
    def get_account_by_client_between(client_id, less_than, greater_than):
        accounts = []
        for account in AccountsDAO.get_accounts_by_client_between(client_id, less_than, greater_than):
            accounts.append(account.serialize())
        return accounts

    @staticmethod
    def get_accounts_by_client(id):
        accounts = []
        for account in AccountsDAO.get_accounts_by_client(id):
            accounts.append(account.serialize())
        return accounts

    @staticmethod
    def delete_account(client_id, account_id):
        update_count = AccountsDAO.delete_account(client_id, account_id)
        return (f"Deleted {update_count} account", 204) if update_count else ("Account not found", 404)

    @staticmethod
    def update_account(client_id, account_id, change_account):
        account = AccountsDAO.get_account(client_id, account_id)
        if account:
            account.account_type = change_account.account_type
            update_count = AccountsDAO.update_account(account)
            return f"Updated {update_count} account", 201
        else:
            return "Account not found", 404

    @staticmethod
    def withdrawal_account(client_id, account_id, amount):
        account = AccountsDAO.get_account(client_id, account_id)
        if account:
            if account.balance - amount > 0:
                account.balance -= amount
                AccountsDAO.update_account(account)
                return (f"{amount} has been withdrawn from {account.account_type}. "
                        f"Current Balance is {account.balance}", 200)
            else:
                return f"Insufficient Funds", 422
        else:
            return "Client or Account not found", 404

    @staticmethod
    def deposit_account(client_id, account_id, amount):
        try:
            account = AccountsDAO.get_account(client_id, account_id)
            if account:
                account.balance += amount
                AccountsDAO.update_account(account)
                return (f"{amount} has been deposited into {account.account_type}. "
                        f"Current Balance is {account.balance}", 200)
            else:
                return "Client or Account not found", 404
        except TypeError as e:
            return "There was an issue processing your request", 400

    @staticmethod
    def transfer_account(client_id, account_id, transfer_account_id, amount):
        account = AccountsDAO.get_account(client_id, account_id)
        transfer_account = AccountsDAO.get_account(client_id, transfer_account_id)
        if account and transfer_account:
            if account.balance - amount > 0:
                account.balance -= amount
                transfer_account.balance += amount
                AccountsDAO.update_account(account)
                AccountsDAO.update_account(transfer_account)
                return f"Successfully Transferred funds", 200
            else:
                return "Insufficient funds", 422
        else:
            return "One or both of those accounts do not exist", 404
