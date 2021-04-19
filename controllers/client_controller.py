import logging

from flask import request, jsonify

import logger
from models.client import Client
from services.client_service import ClientService


def route(app):

    @app.route("/clients/", methods=["GET"])
    def get_all_clients():
        return jsonify(ClientService.get_all_clients()), 200

    @app.route("/clients/<id>/", methods=["GET"])
    def get_client(id):
        client = ClientService.get_client(id)
        if client:
            return client, 200
        else:
            logger.log(f"Client not found with id of {id}", logging.INFO)
            return "Client Not Found", 404

    @app.route("/clients/", methods=["POST"])
    def create_client():
        ClientService.create_client(Client.deserialize(request.json))
        return "Good", 201

    @app.route("/clients/<id>", methods=["PUT"])
    def update_client(id):
        client = Client.deserialize(request.json)
        client.id = id
        update_count = ClientService.update_client(client)
        if update_count > 0:
            return f"Good"
        else:
            logger.log(f"Client could not be updated with an id of {id}")
            return "Client Not Found", 404

    @app.route("/clients/<id>/", methods=["DELETE"])
    def delete_client(id):
        delete_count = ClientService.delete_client(id)
        if delete_count > 0:
            return f"Deleted {delete_count} items", 205
        else:
            logger.log(f"Client could not be deleted with an id of {id}")
            return "Not Found", 404


