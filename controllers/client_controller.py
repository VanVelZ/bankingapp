from flask import request

from models.client import Client
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

