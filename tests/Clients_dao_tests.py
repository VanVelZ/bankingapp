import unittest

from daos.client_dao import ClientDAO
from models.client import Client


class ClientDAOTests(unittest.TestCase):

    client = Client("Test Client")

    def test_insert(self):
        self.assertEqual(ClientDAO.create_client(ClientDAOTests.client), True)

    def test_get_all(self):
        clients = ClientDAO.get_all_clients()
        ClientDAOTests.client = clients.pop()
        self.assertTrue(clients)

    def test_update_client(self):
        ClientDAOTests.client.name = "Updated test client"
        self.assertTrue(ClientDAO.update_client(ClientDAOTests.client))

    def test_get_one(self):
        self.assertTrue(ClientDAO.get_client(ClientDAOTests.client.id))

    def test_delete_client(self):
        client = ClientDAO.get_all_clients().pop()
        self.assertTrue(ClientDAO.delete_client(client.id))


if __name__ == '__main__':
    unittest.main()
