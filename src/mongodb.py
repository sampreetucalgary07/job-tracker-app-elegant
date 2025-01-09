
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi
import os
import sys
from src.utils import load_json



# uri = "mongodb+srv://sampreet-vaidya:fwNSIRqryuVNMLgz@job-tracker.otx6s.mongodb.net/?retryWrites=true&w=majority&appName=Job-tracker"
username = os.environ['db_username']
password = os.environ['db_password']
db_name = os.environ['db_name']
uri = "mongodb+srv://"+ username + ":" + password + "@"+db_name+".otx6s.mongodb.net/?retryWrites=true&w=majority&appName=Job-tracker"

# Create a new client and connect to the server
client = MongoClient(uri, tlsCAFile=certifi.where())


    
    
    

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)