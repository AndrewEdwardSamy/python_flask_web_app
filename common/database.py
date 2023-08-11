import pymongo


class Database(object):
    URI = "***********************************"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['test']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert_one(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)