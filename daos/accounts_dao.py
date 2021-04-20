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
        try:
            sql = "Select * from accounts where id = %s and client_id = %s"
            cursor = connection.cursor()
            cursor.execute(sql, [account_id, client_id])
            record = cursor.fetchone()
            return Account(account_type=record[2], id=record[0], balance=record[3])
        except TypeError:
            return False

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
    def get_accounts_by_client_between(id, less_than, greater_than):
        sql = "Select * from accounts where client_id = %s and balance between %s and %s"
        cursor = connection.cursor()
        cursor.execute(sql, [id, greater_than, less_than])
        records = cursor.fetchall()
        accounts = []

        for record in records:
            accounts.append(Account(account_type=record[2], id=record[0], balance=record[3]))

        return accounts

    @staticmethod
    def update_account(changing_account):
        sql = "Update accounts set account_type=%s, balance=%s where id=%s"
        cursor = connection.cursor()
        cursor.execute(sql, [changing_account.account_type, changing_account.balance, changing_account.id])
        connection.commit()
        return cursor.rowcount

    @staticmethod
    def delete_account(client_id, account_id):
        sql = "Delete from accounts where id = %s and client_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account_id, client_id])
        connection.commit()
        return cursor.rowcount

    @staticmethod
    def create_account(account, client_id):
        try:
            sql = "Insert into accounts values (default, %s, %s, %s)"
            cursor = connection.cursor()
            cursor.execute(sql, [client_id, account.account_type, account.balance])
            connection.commit()
            return "Successfully added Account"
        except:
            return "No client found", 404
        finally:
            connection.commit()

