from flask import Flask



def create_app():
    """Cria e configura uma instância do aplicativo Flask."""

    app = Flask(__name__, template_folder="views/templates")

    # Registra os blueprints (classes de controle)
    from app.controllers.home_controller import HomeController

    app.register_blueprint(HomeController.home)

    #@app.route("/")
    #def hello():
    #    return "Hello, World!"

    app.add_url_rule("/", endpoint="index")

    return app
