from flask import Blueprint, render_template


class HomeController:

    home = Blueprint('home', __name__)

    @home.route("/", methods=["GET"])
    def index():
        return render_template('home/index.html')
