from pymongo import MongoClient
client = MongoClient()

from pprint import pprint
from bson.objectid import ObjectId

if __name__ == '__main__':
    db = client.mongo_db_lab
    collection = db.definitions

    print("-------------------")
    print("| ALL DEFINITIONS |")
    print("-------------------")
    for definition in collection.find():
        pprint(definition)

    print("\n\n--------------------")
    print("| FIRST DEFINITION |")
    print("--------------------")
    pprint(collection.find_one())

    print("\n\n-------------------")
    print("| BARH DEFINITION |")
    print("-------------------")
    for definition in collection.find({"word": "BARH"}):
        pprint(definition)

    print("\n\n-------------------------")
    print("| OBJECT ID QUERY (VCC) |")
    print("-------------------------")
    for definition in collection.find({'_id': ObjectId('56fe9e22bad6b23cde07b940')}):
        pprint(definition)

    print("\n\n---------------------")
    print("| INSERT DEFINITION |")
    print("---------------------")
    definition = {
        "word": "RCOS",
        "definition": "A cool class/club where you can work on some fun projects"
    }
    definition_id = collection.insert_one(definition).inserted_id
    for definition in collection.find({'_id': definition_id}):
        pprint(definition)

