import pymongo
from bson.objectid import ObjectId
from collections.abc import MutableMapping


class MongoDBConnector:
    def __init__(self, url: str = "mongodb://localhost:27017", db_name: str = "db"):
        self._url = url
        self._db_name = db_name
        self._conn = pymongo.MongoClient(self._url)
        self._db = self._conn[self._db_name]

    def insert(self, collection: str, document: MutableMapping) -> ObjectId:
        return self._db[collection].insert_one(document).inserted_id
    
    def find(self, collection: str, query: MutableMapping) -> list:
        return [document for document in self._db[collection].find(query)]

    def exit(self) -> None:
        self._conn.close()
