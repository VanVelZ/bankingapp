import unittest

from models.client import Client
from services.client_service import ClientService


class ClientServiceTest(unittest.TestCase):

    client = Client("Test Client")

    def test_01_insert(self):
        self.assertTrue(ClientService.create_client(ClientServiceTest.client))

    def test_02_get_all(self):
        clients = ClientService.get_all_clients()
        ClientServiceTest.client = Client.deserialize(clients.pop())
        self.assertTrue(clients)

    def test_03_get_one(self):
        self.assertTrue(ClientService.get_client(ClientServiceTest.client.id))

    def test_93_update(self):
        ClientServiceTest.client.name = "Updated Test Client"
        self.assertTrue(ClientService.update_client(ClientServiceTest.client))

    def test_94_delete(self):
        self.assertTrue(ClientService.delete_client(ClientServiceTest.client.id))


if __name__ == '__main__':
    unittest.main()
