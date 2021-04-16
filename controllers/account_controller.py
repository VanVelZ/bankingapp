
def route(app):

    @app.route("/accounts", methods=["GET"])
    def get_all_accounts():
        return "Still need to get accounts"

    @app.route("/accounts/<id>", methods=["GET"])
    def get_account(id):
        return f"Still need to get accounts for {id}"

    @app.route("/accounts", methods=["PUSH"])
    def create_account(account):
        return "Still need to create accounts"

    @app.route("/accounts", methods=["PUT"])
    def update_account(account):
        return "Still need to update accounts"

    @app.route("/accounts/<id>", methods=["DELETE"])
    def update_account(account):
        return "Still need to delete accounts"
