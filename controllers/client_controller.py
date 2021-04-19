from flask import request, jsonify

from models.client import Client
from services.account_service import AccountService
from services.client_service import ClientService


def route(app):

    @app.route("/clients/", methods=["GET"])
    def get_all_clients():
        return jsonify(ClientService.get_all_clients()), 200

    @app.route("/clients/<id>/", methods=["GET"])
    def get_client(id):
        try:
            return ClientService.get_client(id), 200
        except:
            return "Client Not Found", 404

    @app.route("/clients/", methods=["POST"])
    def create_client():
        ClientService.create_client(Client.deserialize(request.json))
        return "Good", 201

    @app.route("/clients/<id>", methods=["PUT"])
    def update_client(id):
        client = Client.deserialize(request.json)
        client.id = id
        try:
            ClientService.update_client(client)
            return "Good"
        except:
            return "Client Not Found", 404

    @app.route("/clients/<id>/", methods=["DELETE"])
    def delete_client(id):
        delete_count = ClientService.delete_client(id)
        if delete_count > 0:
            return f"Deleted {delete_count} items", 205
        else:
            return "Not Found", 404


