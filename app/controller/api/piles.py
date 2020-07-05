from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import (
    Blueprint, request
)
from app.db import db
from app.controller.errors import (
    bad_request, internal_server, not_found
)
from app.controller.api import api

piles = db.piles
entries = db.entries


@api.route('/piles', methods=['GET'])
def list_piles():
    return dumps([pile for pile in piles.find()])


@api.route('/piles/<id>', methods=['GET'])
def get_pile(id):
    return dumps(piles.find_one(ObjectId(id)))


@api.route('/piles/<id>/entries', methods=['GET'])
def list_entries_by_pile_id(id):
    return dumps([entry for entry in entries.find({'pile_id': ObjectId(id)})])


@api.route('/piles', methods=['POST'])
def create_pile():
    data = request.get_json() or {}
    return (dumps(piles.insert_one(data).inserted_id), 201) \
        if data else bad_request('Invalid data')
