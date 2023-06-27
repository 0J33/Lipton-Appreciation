import os
from pymongo import MongoClient
try:
    from .env import *
except:
    connection_string = os.getenv('connection_string')
    db_name = os.getenv('db_name')
    collection_name = os.getenv('collection_name')
    
# Establish a connection to the MongoDB server
client = MongoClient(connection_string)
    
# Access a specific database
db = client[db_name]

# Access a specific collection
collection = db[collection_name]

def insert(collection, recipient, sender, message):
    print(recipient, sender, message)
    # Insert a document
    document = {'recipient': recipient, 'sender': sender, 'message': message}
    collection.insert_one(document)

def get_all(collection, recipient):
    # Query documents
    result = collection.find({'recipient': recipient})
    res = []
    for document in result:
        res.append(document)
    return res

def get_messages(collection, recipient):
    documents = get_all(collection, recipient)
    res = []
    for document in documents:
        res.append([document['sender'], document['message']])
    return res