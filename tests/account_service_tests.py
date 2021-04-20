import unittest
from models.account import Account
from services.account_service import AccountService


class AccountServiceTest(unittest.TestCase):

    account = Account("Test Account", balance=4000)

    def test_00_create(self):
        self.assertTrue(AccountService.create_account(AccountServiceTest.account, 1))

    def test_01_get_all(self):
        accounts = AccountService.get_accounts_by_client(1)
        AccountServiceTest.account = Account.deserialize(accounts.pop())
        self.assertTrue(accounts)

    def test_02_get_one(self):
        self.assertTrue(AccountService.get_account(1, AccountServiceTest.account.id))

    def test_03_update(self):
        account = Account("Updated Test Account", balance=4000)
        response = AccountService.update_account(1, AccountServiceTest.account.id, account)
        self.assertEqual(response[1], 201)

    def test_04_withdraw(self):
        response = AccountService.withdrawal_account(1, AccountServiceTest.account.id, 400)
        self.assertEqual(response[1], 200)

    def test_05_deposit(self):
        response = AccountService.deposit_account(1, AccountServiceTest.account.id, 400)
        self.assertEqual(response[1], 200)

    def test_06_transfer(self):
        response = AccountService.transfer_account(1, AccountServiceTest.account.id,
                                                   AccountServiceTest.account.id, 400)
        self.assertEqual(response[1], 200)

    def test_07_delete(self):
        response = AccountService.delete_account(1, AccountServiceTest.account.id)
        self.assertEqual(response[1], 204)


if __name__ == '__main__':
    unittest.main()
