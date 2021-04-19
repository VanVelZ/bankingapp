from models.account import Account
from utils.db_connection import connection


class AccountsDAO:

    @staticmethod
    def get_all_accounts():
        sql = "Select * from accounts"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        accounts = []

        for record in records:
            accounts.append(Account(account_type=record[2], id=record[0], balance=record[3]))

        return accounts

    @staticmethod
    def get_account(client_id, account_id):
        sql = "Select * from accounts where id = %s and client_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account_id, client_id])
        record = cursor.fetchone()
        return Account(account_type=record[2], id=record[0], balance=record[3])

    @staticmethod
    def get_accounts_by_client(id):
        sql = "Select * from accounts where client_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [id])
        records = cursor.fetchall()
        accounts = []

        for record in records:
            accounts.append(Account(account_type=record[2], id=record[0], balance=record[3]))

        return accounts

    @staticmethod
    def update_account(changing_account):
        sql = "Update accounts set account_type=%s, balance=%s where id=%s"
        cursor = connection.cursor()
        cursor.execute(sql, [changing_account.id, changing_account.account_type, changing_account.balance])
        connection.commit()
        return cursor.rowcount

    @staticmethod
    def delete_account(id):
        sql = "Delete from accounts where id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [id])
        connection.commit()
        return cursor.rowcount

    @staticmethod
    def create_account(account):
        sql = "Insert into accounts values (default, %s, %s)"
        cursor = connection.cursor()
        cursor.execute(sql, [account.account_type, account.balance])
        connection.commit()
        return True


if __name__ == '__main__':
    print(AccountsDAO.get_all_accounts()[0])
    print(AccountsDAO.get_account(1).id)
    print(AccountsDAO.create_account(Account("Dummy Account", 100)))
    print(AccountsDAO.get_all_accounts()[3])
    print(AccountsDAO.update_account(Account(4, "Smarty Account", 0)))
    print(AccountsDAO.get_all_accounts()[3])
    print(AccountsDAO.delete_account(4))
    print(AccountsDAO.get_all_accounts())
