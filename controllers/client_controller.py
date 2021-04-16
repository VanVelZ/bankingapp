
def route(app):

    @app.route("/clients", methods=["GET"])
    def get_all_clients():
        return "Still need to get clients"

    @app.route("/clients/<id>", methods=["GET"])
    def get_client(id):
        return f"Still need to get clients for {id}"

    @app.route("/clients", methods=["PUSH"])
    def create_client(client):
        return "Still need to create clients"

    @app.route("/clients", methods=["PUT"])
    def update_client(client):
        return "Still need to update clients"

    @app.route("/clients/<id>", methods=["DELETE"])
    def update_client(client):
        return "Still need to delete clients"

