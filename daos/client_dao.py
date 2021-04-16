from daos.accounts_dao import AccountsDAO
from models.client import Client
from utils.db_connection import connection


class ClientDAO:

    @staticmethod
    def get_all_clients():
        sql = "Select id, name from clients"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        clients = []

        for record in records:
            clients.append(Client(id=record[0], name=record[1], accounts=AccountsDAO.get_accounts_by_client(record[0])))

        return clients

    @staticmethod
    def get_client(id):
        sql = "Select id, name from clients where id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [id])
        record = cursor.fetchone()

        return Client(id=record[0], name=record[1], accounts=AccountsDAO.get_accounts_by_client(record[0]))

    @staticmethod
    def update_client(changing_client):
        sql = "Update clients set name=%s where id=%s"
        cursor = connection.cursor()
        cursor.execute(sql, [changing_client.id, changing_client.name])
        connection.commit()
        return changing_client

    @staticmethod
    def delete_client(id):
        sql = "Delete from clients where id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [id])
        connection.commit()
        return True

    @staticmethod
    def create_client(client):
        sql = "Insert into clients values (default, %s)"
        cursor = connection.cursor()
        cursor.execute(sql, [client.name])
        connection.commit()
        return True


if __name__ == '__main__':
    print(ClientDAO.get_all_clients())
    print(ClientDAO.get_client(1).accounts[0].balance)


#inserted comment to test git import
