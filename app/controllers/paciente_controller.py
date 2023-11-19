from flask import Blueprint, render_template


class PacienteController:

    paciente = Blueprint('paciente', __name__, url_prefix="/paciente")

    @paciente.route("/", methods=["GET", "POST"])
    def index():
        return render_template("paciente/index.html")




