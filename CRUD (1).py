from pymongo import MongoClient
from bson.objectid import ObjectId
from pymongo.errors import OperationFailure


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password, host, port, db, collection):
        # Connection Variables (replace with your actual credentials if different)
        USER = 'aacSushma'
        PASS = 'sushma1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31241
        DB = 'AAC'
        COL = 'animals'
        
        # Initialize Connection
        self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}/?authSource=admin')
        self.database = self.client[DB]
        self.collection = self.database[COL]
        
        # Check connection by pinging the MongoDB server
        try:
            self.client.admin.command('ping')  # Ping to check the connection
            print("Connection successful")
        except OperationFailure as e:
            print(f"Connection failed: {e}")
    # Create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            try:
                result = self.collection.insert_one(data)  # data should be a dictionary
                return result.acknowledged
            except OperationFailure as e:
                print(f"Error inserting document: {e}")
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Read method to implement the R in CRUD.
    def read(self, data=None):
        try:
            if data is not None:
                return list(self.collection.find(data))  # Returns all matching documents as a list
            else:
                return list(self.collection.find())  # Returns all documents if no filter is provided
        except OperationFailure as e:
            print(f"Error reading documents: {e}")
            return []

    # Update method to implement the U in CRUD.
    def update(self, query, new_values):
        if query is not None and new_values is not None:
            try:
                result = self.collection.update_many(query, {"$set": new_values})
                return result.modified_count > 0  # Returns True if documents were modified
            except OperationFailure as e:
                print(f"Error updating documents: {e}")
                return False
        else:
            raise Exception("Both query and new_values must be provided for update")

    # Delete method to implement the D in CRUD.
    def delete(self, query):
        if query is not None:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count > 0  # Returns True if documents were deleted
            except OperationFailure as e:
                print(f"Error deleting documents: {e}")
                return False
        else:
            raise Exception("Query parameter is required for delete operation")
