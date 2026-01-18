import os
import sys
import json
import certifi
import pandas as pd
import numpy as np
import pymongo
import certifi

from dotenv import load_dotenv
load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")

ca = certifi.where()

from networksecurity.exception.exception import NetworkSecurityException

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys.exc_info())

    @staticmethod
    def csv_to_json(file_path):
        """
        Convert CSV file to JSON records list.

        Args:
            file_path (str): Path to the input CSV file.
        """
        try:
            df = pd.read_csv(file_path)
            df.reset_index(drop=True, inplace=True)
            records = list(json.loads(df.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys.exc_info())
    def insert_data_mongodb(self, record, database, collection):
        """
        Insert data into MongoDB collection.

        Args:
            record (list): List of records to be inserted.
            database (str): Name of the database.
            collection (str): Name of the collection.
        """
        try:
            self.database = database
            self.collection = collection
            self.record = record
            self.mongo_client = pymongo.MongoClient(MONGODB_URI)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.record)
            return (len(self.record))
        except Exception as e:
            raise NetworkSecurityException(e, sys.exc_info())

if __name__ == "__main__":
    file_path = "network_data/phishingData.csv"
    Database = "NetworkSecurityDB"
    Collection = "PhishingDataCollection"
    networkobj = NetworkDataExtract()
    record = networkobj.csv_to_json(file_path)
    print(f"Total records to be inserted: {record}")
    no_of_records = networkobj.insert_data_mongodb(record, Database, Collection)
    print(f"No of records inserted: {no_of_records}")