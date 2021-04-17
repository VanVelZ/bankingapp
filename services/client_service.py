from daos.client_dao import ClientDAO


class ClientService:

    @staticmethod
    def create_client(client):
        return ClientDAO.create_client(client)

    @staticmethod
    def get_all_clients():
        pass

    @staticmethod
    def get_client(id):
        pass

    @staticmethod
    def delete_client(id):
        pass

    @staticmethod
    def update_client(client):
        pass
