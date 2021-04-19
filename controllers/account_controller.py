from flask import jsonify

from services.account_service import AccountService


def route(app):

    @app.route("/clients/<client_id>/accounts/", methods=["GET"])
    def get_accounts(client_id):
        return jsonify(AccountService.get_account_by_client(client_id))

    @app.route("/clients/<client_id>/accounts/<account_id>/", methods=["GET"])
    def get_account(client_id, account_id):
        return AccountService.get_account(client_id, account_id)

    @app.route("/clients/<clientId>/accounts/", methods=["GET"])
    def get_accounts_between(client_id, less_than, greater_than):
        return "Not implemented"

    # @app.route("/clients/<clientId>/accounts/<accountId>/", methods=["PATCH"])
    # def edit_account_balance(client_id, account_id):
    #     return "Not implemented"
    #
    # @app.route("/clients/<clientId>/accounts/<accountId/transfer/<transferId>", methods=["PATCH"])
    # def transfer_money(client_id, account_id, transfer_id):
    #     return "Not implemented"
