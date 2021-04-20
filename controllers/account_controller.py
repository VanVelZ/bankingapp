from flask import jsonify, request

import logger
from models.account import Account
from services.account_service import AccountService


def route(app):

    @app.route("/clients/<client_id>/accounts/", methods=["POST"])
    def add_account(client_id):
        account = Account.deserialize(request.json)
        return AccountService.create_account(account, client_id)

    @app.route("/clients/<client_id>/accounts/<account_id>", methods=["PUT"])
    def edit_account(client_id, account_id):
        account = Account.deserialize(request.json)
        return AccountService.update_account(client_id, account_id, account)

    @app.route("/clients/<client_id>/accounts/<account_id>", methods=["DELETE"])
    def delete_account(client_id, account_id):
        update_count = AccountService.delete_account(client_id, account_id)
        return (f"Deleted {update_count} account", 204) if update_count else ("Account not found", 404)

    @app.route("/clients/<client_id>/accounts/", methods=["GET"])
    def get_accounts(client_id):
        less_than = request.args.get('amountLessThan')
        greater_than = request.args.get('amountGreaterThan')
        accounts = []
        if less_than is not None and greater_than is not None:
            accounts = AccountService.get_account_by_client_between(client_id, less_than, greater_than)
        else:
            accounts = AccountService.get_accounts_by_client(client_id)

        return (jsonify(accounts), 200) if accounts else ("Accounts Not Found", 404)

    @app.route("/clients/<client_id>/accounts/<account_id>/", methods=["GET"])
    def get_account(client_id, account_id):
        return AccountService.get_account(client_id, account_id)

    @app.route("/clients/<client_id>/accounts/<account_id>/", methods=["PATCH"])
    def edit_account_balance(client_id, account_id):

        action = request.json["action"]

        if action == 'withdraw':
            return AccountService.withdrawal_account(client_id, account_id, request.json["amount"])
        elif action == 'deposit':
            return AccountService.deposit_account(client_id, account_id, request.json["amount"])
        else:
            return """Body must contain a JSON with an action property and values of withdrawal or deposit and
                      an amount property with a valid number""", 400

    @app.route("/clients/<client_id>/accounts/<account_id>/transfer/<transfer_account_id>", methods=["PATCH"])
    def transfer_money(client_id, account_id, transfer_account_id):

        amount = request.json["amount"]

        if float(amount) > 0:
            return AccountService.transfer_account(client_id, account_id, transfer_account_id, amount)
        else:
            logger.log(f"Unable to complete a transfer of {amount} between accounts {account_id} "
                       f"and {transfer_account_id}")
            return """Body must contain a JSON with an amount property that is a number greater than 0""", 400
