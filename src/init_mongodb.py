from pymongo.mongo_client import MongoClient
import os
import certifi
import pandas as pd
from utils import load_json

env_variables = load_json("./env_variable.json")

username = env_variables["db_username"]
password = env_variables["db_password"]
db_name = env_variables["db_name"]
collection_name = env_variables["collection_name"]

uri = "mongodb+srv://"+ username + ":" + password + "@"+db_name+".otx6s.mongodb.net/?retryWrites=true&w=majority&appName=Job-tracker"

# Create a new client and connect to the server
client = MongoClient(uri, tlsCAFile=certifi.where())
df = pd.read_csv("./data/init_applications.csv")
db = client[db_name]
collection = db[collection_name]
collection.delete_many({})
collection.insert_many(df.to_dict('records'))
