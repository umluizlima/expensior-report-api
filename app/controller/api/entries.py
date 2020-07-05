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

entries = db.entries


@api.route('/entries', methods=['GET'])
def list_entries():
    return dumps([entry for entry in entries.find()])


@api.route('/entries/<pile_id>', methods=['GET'])
def list_entries_by_pile(pile_id):
    return dumps([entry for entry in entries.find()])


@api.route('/entries', methods=['POST'])
def create_entry():
    data = request.get_json() or {}
    data['pile_id'] = ObjectId(data['pile_id'])
    return (dumps(entries.insert_one(data).inserted_id), 201) \
        if data else bad_request('Invalid data')
