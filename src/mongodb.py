
from pymongo.mongo_client import MongoClient
import certifi
import os
import streamlit as st
import pandas as pd
# from pymongo.server_api import ServerApi
#from src.utils import load_json


# env_variables = load_json("./env_variable.json")


print(st.secrets)
client = MongoClient(f"mongodb+srv://{st.secrets['MONGODB_USERNAME']}:{st.secrets['MONGODB_PASSWORD']}@{st.secrets['MONGODB_HOST']}/?retryWrites=true&w=majority&appName=<AppName>", #)
                     tlsCAFile=certifi.where()) # --> If Local Connection

db_name = os.environ["db_name"]#env_variables["db_name"]
collection_name = os.environ["collection_name"]#env_variables["collection_name"]

#@st.cache_resource
def update_mongodb_db(df):
    df.fillna("2025-01-09",inplace=True)
    db = client[db_name]
    collection = db[collection_name]
    collection.delete_many({})
    try:
        collection.insert_many(df.to_dict('records'))
    except ValueError as e:
        st.error("Error in updating the database")
        st.write(e)
    
    
@st.cache_resource (ttl=200)
def read_mongodb_db():
    db = client[st.secrets['db_name']]
    collection = db[st.secrets['collection_name']]
    # st.success("Connected to the databasE")
    items = collection.find()
    return pd.DataFrame(list(items))

