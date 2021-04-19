from daos.client_dao import ClientDAO


class ClientService:

    @staticmethod
    def create_client(client):
        return ClientDAO.create_client(client)

    @staticmethod
    def get_all_clients():
        clients = []
        for client in ClientDAO.get_all_clients():
            clients.append(client.serialize())
        return clients

    @staticmethod
    def get_client(id):
        return ClientDAO.get_client(id).serialize()

    @staticmethod
    def delete_client(id):
        return ClientDAO.delete_client(id)

    @staticmethod
    def update_client(client):
        return ClientDAO.update_client(client)
