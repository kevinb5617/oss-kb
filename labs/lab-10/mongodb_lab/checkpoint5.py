from pymongo import MongoClient
client = MongoClient()

db = client.mongo_db_lab
collection = db.definitions

from pprint import pprint
from bson.objectid import ObjectId

import random
import datetime

def random_word_requester():
    definition_list = []
    for definition in collection.find():
        definition_list.append(definition)

    rand_def = random.choice(definition_list)
    
    collection.update_one({"_id": rand_def["_id"]}, {"$push": {"dates": str(datetime.datetime.isoformat(datetime.datetime.utcnow()))}})
    return collection.find_one({"_id": rand_def["_id"]})


if __name__ == '__main__':
    pprint(random_word_requester())
