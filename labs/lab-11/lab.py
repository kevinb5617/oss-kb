from pymongo import MongoClient
client = MongoClient()

db = client.mongo_db_lab
collection = db.definitions

from pprint import pprint
from bson.objectid import ObjectId

import random
import datetime

def update_RPI():
    for entry in collection.find({"definition": {"$regex": " RPI "}}):
        definition = entry["definition"]
        definition = definition.replace(" RPI ", " Rensselaer Polytechnic Institute ")
        collection.update_one({"_id": entry["_id"]}, {"$set": {"definition": definition}})


if __name__ == '__main__':
    update_RPI()
