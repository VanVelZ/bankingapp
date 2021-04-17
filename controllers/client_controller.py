from flask import request

from models.client import Client
from services.account_service import AccountService
from services.client_service import ClientService


def route(app):

    @app.route("/clients/", methods=["GET"])
    def get_all_clients():
        return ClientService.get_all_clients()

    @app.route("/clients/<id>/", methods=["GET"])
    def get_client(id):
        return ClientService.get_client(id)

    @app.route("/clients/", methods=["POST"])
    def create_client(client):
        return ClientService.create_client(client)

    @app.route("/clients/<id>", methods=["PUT"])
    def update_client(id):
        client = Client.deserialize(request.json)
        client.id = id
        return update_client(client)

    @app.route("/clients/<id>/", methods=["DELETE"])
    def delete_client(id):
        return ClientService.delete_client(id)

    @app.route("/clients/<clientId>/accounts/", ["POST"])
    def create_account(client_id):
        return "Not implemented"

    @app.route("/clients/<clientId>/accounts/", ["GET"])
    def get_accounts(client_id):
        return AccountService.get_account_by_client(client_id)

    @app.route("/clients/<clientId>/accounts/<accountId>/", ["GET"])
    def get_account(client_id, account_id):
        return "Not implemented"

    @app.route("/clients/<clientId>/accounts/", ["GET"])
    def get_accounts_between(client_id, less_than, greater_than):
        return "Not implemented"

    @app.route("/clients/<clientId>/accounts/<accountId>/", ["PATCH"])
    def edit_account_balance(client_id, account_id):
        return "Not implemented"

    @app.route("/clients/<clientId>/accounts/<accountId/transfer/<transferId>")
    def transfer_money(client_id, account_id, transfer_id):
        return "Not implemented"
