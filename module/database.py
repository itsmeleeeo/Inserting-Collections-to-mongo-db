import configparser
from pymongo import MongoClient

def getConfig():
    print('Reading config file!')
    config = configparser.ConfigParser()
    config.readfp(open(r'mongo.conf'))

    return config

def connect(config):
    host = config.get('mongo', 'host')
    database = config.get('mongo', 'database')
    collection = config.get('mongo', 'collection')
    port = config.get('mongo', 'port')

    dbUri = "mongodb://" + host + ":" + port + "/" + database

    print("Attempting to connect to: " + dbUri)

    client = MongoClient(dbUri)
    return client[database]