from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initialize Connection
        # Make sure to update the host and port if your local setup differs
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        USER = username
        PASS = password
        
        # Initialize MongoClient
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client['aac']

    def create(self, data):
        """ Method to implement the C in CRUD. """
        if data is not None:
            insert_result = self.database.animals.insert_one(data)  # data should be dictionary
            return True if insert_result.inserted_id else False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    def read(self, query):
        """ Method to implement the R in CRUD. """
        if query is not None:
            # Returns a cursor pointing to the matched documents
            cursor = self.database.animals.find(query)
            return list(cursor)
        else:
            raise Exception("Nothing to read, because query parameter is empty")

    def update(self, query, update_data):
        """ Method to implement the U in CRUD. """
        if query is not None and update_data is not None:
            # Update all documents matching the query
            update_result = self.database.animals.update_many(query, {"$set": update_data})
            return update_result.modified_count
        else:
            raise Exception("Query or update data is empty")

    def delete(self, query):
        """ Method to implement the D in CRUD. """
        if query is not None:
            # Delete all documents matching the query
            delete_result = self.database.animals.delete_many(query)
            return delete_result.deleted_count
        else:
            raise Exception("Nothing to delete, because query parameter is empty")