import os
from flask import Flask, request, jsonify


def create_app():
    app = Flask(__name__)

    from flask_cors import CORS
    CORS(app)

    from flask_sslify import SSLify
    if 'DYNO' in os.environ:  # only trigger SSLify if app is running on Heroku
        sslify = SSLify(app)

    # register blueprints
    from app.controller.api import api
    app.register_blueprint(api)

    return app
