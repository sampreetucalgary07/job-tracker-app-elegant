from pymongo.mongo_client import MongoClient
import os
import certifi
import pandas as pd
#from utils import load_json
import streamlit as st  
from pymongo.server_api import ServerApi

#env_variables = load_json("./env_variable.json")

client = MongoClient(f"mongodb+srv://{st.secrets['MONGODB_USERNAME']}:{st.secrets['MONGODB_PASSWORD']}@{st.secrets['MONGODB_HOST']}/?retryWrites=true&w=majority&appName=<AppName>", #)
                     tlsCAFile=certifi.where()) # --> If Local Connection

# Create a new client and connect to the server
#client = MongoClient(uri, tlsCAFile=certifi.where())
df = pd.read_csv("./data/init_applications.csv")
db = client[st.secrets['db_name']]
collection = db[st.secrets['collection_name']]
collection.delete_many({})
collection.insert_many(df.to_dict('records'))
