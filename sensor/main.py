from sensor.configuration.mongo_db_connection import MongoClient


if __name__ == "__main__":

    mongodb_client = MongoClient()
    print("Mongo DB Connections :", mongodb_client.database.list_collection_names())