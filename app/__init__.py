import os
from flask import Flask, request, jsonify
from pymongo import MongoClient


def create_app():
    app = Flask(__name__)

    client = MongoClient(
        os.environ.get('MONGODB_URI') \
        or 'mongodb://localhost:27017/expensior'
    )
    db = client.get_database()
    piles = db.piles_collection

    from flask_cors import CORS
    CORS(app)

    from flask_sslify import SSLify
    if 'DYNO' in os.environ:  # only trigger SSLify if app is running on Heroku
        sslify = SSLify(app)

    @app.route("/")
    def home():
        return "Welcome home."


    @app.route("/api/entries", methods=['POST'])
    def create_entry():
        data = request.get_json() or {}
        return (str(entries.insert_one(data).inserted_id), 201) \
            if data \
            else ('Bad Request', 400)


    @app.route("/api/piles", methods=['POST'])
    def create_pile():
        data = request.get_json() or {}
        response = ('Bad Request', 400)
        if data:
            data['entries'] = []
            response = (str(piles.insert_one(data).inserted_id), 201)
        return response


    @app.route("/api/piles", methods=['GET'])
    def get_piles():
        return jsonify(
            [{'name': pile['name'], 'entries': pile['entries']} \
            for pile \
            in piles.find()])

    return app
