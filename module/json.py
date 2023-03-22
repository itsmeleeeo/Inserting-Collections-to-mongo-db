import json
from module import database

def InsertJson(db):
    config = database.getConfig()
    cars = db['cars']
    loadFile = config.get('data_files', 'json_file')

    with open(loadFile, 'r') as file:
        jsonContent = json.load(file)
        
        for c in jsonContent:
            cars.insert_one(c)
            print(c)