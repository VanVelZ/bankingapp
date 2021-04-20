import unittest

from daos.accounts_dao import AccountsDAO
from models.account import Account


class AccountsDAOTests(unittest.TestCase):

    account = Account("Test Account", balance=50)

    def test_account_insert(self):
        self.assertTrue(AccountsDAO.create_account(AccountsDAOTests.account, 1))

    def test_account_get_all(self):
        accounts = AccountsDAO.get_all_accounts()
        AccountsDAOTests.account = accounts.pop()
        self.assertTrue(accounts)

    def test_account_get_by_client(self):
        self.assertTrue(AccountsDAO.get_accounts_by_client(1))

    def test_account_get_one(self):
        self.assertTrue(AccountsDAO.get_account(1, AccountsDAOTests.account.id))

    def test_account_update(self):
        AccountsDAOTests.account.account_type = "Updated Test Account"
        self.assertTrue(AccountsDAO.update_account(AccountsDAOTests.account))

    def test_account_zdelete(self):
        self.assertTrue(AccountsDAO.delete_account(1, AccountsDAOTests.account.id))

    def test_account_get_between(self):
        self.assertTrue(AccountsDAO.get_accounts_by_client_between(1, 100, 0))


if __name__ == '__main__':
    unittest.main()
