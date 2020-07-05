import os
from pymongo import MongoClient

client = MongoClient(os.environ.get('MONGODB_URI') \
    or 'mongodb://localhost:27017/expensior')
db = client.get_database()
