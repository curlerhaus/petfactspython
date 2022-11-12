# Config
from flask import Flask, request

# Factory function


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "Hello, Petfax!"

    from . import pet
    app.register_blueprint(pet.bp)

    return app
