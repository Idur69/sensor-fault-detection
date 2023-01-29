import pymongo
import certifi
from sensor.constant.database import DATABASE_NAME

ca = certifi.where()

class MongoDBClient:
    client  = None

    def __init__(self, database_name = DATABASE_NAME)->None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = "mongodb+srv://idur:mdbidur123@cluster0.cpwdu.mongodb.net/admin?authSource=admin&replicaSet=atlas-r5dgc3-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true"
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise e