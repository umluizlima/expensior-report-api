import os
from flask import Flask, request, jsonify
from pymongo import MongoClient


def create_app():
    app = Flask(__name__)

    client = MongoClient(
        os.environ.get('DATABASE_URL')
        or 'mongodb://localhost:27017/'
    )
    db = client.expensior_database
    entries = db.entries_collection

    @app.route("/")
    def home():
        return "Welcome home."


    @app.route("/api/entries", methods=['POST'])
    def create_entry():
        data = request.get_json() or {}
        return (str(entries.insert_one(data).inserted_id), 201) \
            if data \
            else ('Bad Request', 400)

    return app
