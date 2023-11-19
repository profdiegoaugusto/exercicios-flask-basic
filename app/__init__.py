from flask import Flask

from app.controllers.paciente_controller import PacienteController


def create_app():
    """Cria e configura uma instância do aplicativo Flask."""

    app = Flask(__name__, template_folder="views/templates")

    # Registra os blueprints (classes de controle)
    from app.controllers.home_controller import HomeController

    app.register_blueprint(HomeController.home)
    app.register_blueprint(PacienteController.paciente)

    app.add_url_rule("/", endpoint="home.index")

    return app
