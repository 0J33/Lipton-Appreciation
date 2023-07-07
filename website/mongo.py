import os
from pymongo import MongoClient
try:
    from .env import *
except:
    collection_name = os.getenv('collection_name')
    db_name = os.getenv('db_name')
    connection_string = os.getenv('connection_string')
    
# Establish a connection to the MongoDB server
client = MongoClient(connection_string)
    
# Access a specific database
db = client[db_name]

# Access a specific collection
collection = db[collection_name]

def insert(collection, recipient, sender, message):
    # Check if the recipient document exists
    existing_document = collection.find_one({'recipient': recipient})

    if existing_document:
        # Append the sender and message to the existing document's 'messages' attribute
        collection.update_one(
            {'_id': existing_document['_id']},
            {'$push': {'messages': {'sender': sender, 'message': message}}}
        )
    else:
        # Create a new document and append the sender and message
        document = {
            'recipient': recipient,
            'messages': [{'sender': sender, 'message': message}]
        }
        collection.insert_one(document)

def get_messages(collection, recipient):
    recipient_document = collection.find_one({'recipient': recipient})

    if recipient_document:
        # Access the 'messages' attribute and convert it to a list of lists
        messages = recipient_document.get('messages', [])
        return [[message['sender'], message['message']] for message in messages]
    else:
        return []
    
def delete(collection, recipient):
    # Delete the document with the given recipient
    collection.delete_one({'recipient': recipient})
    
def number_of_messages(collection):
    # Return the number of messages in all documents in the collection (each document has attribute 'messages' which is a list of messages)
    return sum([len(document['messages']) for document in collection.find()])

