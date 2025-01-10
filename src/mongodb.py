
from pymongo.mongo_client import MongoClient
import certifi
import os
import streamlit as st
import pandas as pd
from pymongo.server_api import ServerApi
#from src.utils import load_json


# env_variables = load_json("./env_variable.json")

username = os.environ["db_username"] #env_variables["db_username"]
password = os.environ[ "db_password"]#env_variables["db_password"]
db_name = os.environ["db_name"]#env_variables["db_name"]
collection_name = os.environ["collection_name"]#env_variables["collection_name"]
uri = "mongodb+srv://"+ username + ":" + password + "@"+db_name+".otx6s.mongodb.net/?retryWrites=true&w=majority&appName=Job-tracker"

# Create a new client and connect to the server


#@st.cache_resource
def update_mongodb_db(df):
    df.fillna("2025-01-09",inplace=True)
    #client = MongoClient(uri, tlsCAFile=certifi.where())
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client[db_name]
    collection = db[collection_name]
    collection.delete_many({})
    try:
        collection.insert_many(df.to_dict('records'))
    except ValueError as e:
        st.error("Error in updating the database")
        st.write(e)
    
    
#@st.cache_resource (ttl=600)
def read_mongodb_db():
    
    client = MongoClient(uri, tlsCAFile=certifi.where())
    db = client[db_name]
    collection = db[collection_name]
    items = collection.find()
    return pd.DataFrame(list(items))

