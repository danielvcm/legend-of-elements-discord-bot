import pymongo
import os
from dotenv import load_dotenv

load_dotenv()
class MongoDB:
    def __init__(self):
        self.database = None

    def connect(self):
        mongo = pymongo.MongoClient(host=os.getenv('MONGODB_HOST'), port=int(os.getenv('MONGODB_PORT')), username=os.getenv('MONGODB_USER'), password=os.getenv('MONGODB_PASSWORD') ,connect=True)
        self.database = mongo[os.getenv('MONGODB_DATABASE')]
        return self.database

