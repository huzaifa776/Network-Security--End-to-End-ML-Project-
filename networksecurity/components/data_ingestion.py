from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.artifact_entity import DataIngestionArtifact

#Configuration of the data ingestion component
from networksecurity.entity.config_entity import DataIngestionConfig
import os
import sys
import pymongo
from typing import List
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

# Prefer the same env key used by test_mongodb.py
MONGODB_URI = os.getenv("MONGODB_URI")

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise NetworkSecurityException(e, sys.exc_info()) from e
        
    def export_collection_as_dataframe(self) -> pd.DataFrame:
        """
        Method Name :   export_collection_as_dataframe
        Description :   This method exports the MongoDB collection data as a pandas DataFrame.

        Output      :   pd.DataFrame
        On Failure  :   Raise Exception
        """
        try:
            if not MONGODB_URI:
                raise NetworkSecurityException(
                    Exception("Environment variable MONGODB_URI is not set"),
                    sys.exc_info()
                )
            data_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name
            self.mongo_client = pymongo.MongoClient(
                MONGODB_URI,
                serverSelectionTimeoutMS=5000  # fail fast if MongoDB is unreachable
            )
            collection = self.mongo_client[data_name][collection_name]
            df = pd.DataFrame(list(collection.find()))
            
            if df.empty:
                raise Exception(
                    f"No data found in MongoDB collection '{collection_name}' in database '{data_name}'. "
                    "Please ensure data has been pushed to MongoDB using push_data.py or populate the collection."
                )
            
            logging.info(f"Fetched {len(df)} records from MongoDB collection '{collection_name}'")
            
            if "_id" in df.columns:
                df = df.drop(columns=["_id"], axis=1)
            df.replace(to_replace="NaN", value=np.nan, inplace=True)
            return df
        except Exception as e:
            raise NetworkSecurityException(e, sys.exc_info()) from e
        
    def export_data_into_feature_store(self, dataframe: pd.DataFrame) -> str:
        """
        Method Name :   export_data_into_feature_store
        Description :   This method exports the DataFrame into a feature store as a CSV file.

        Output      :   str (file path)
        On Failure  :   Raise Exception
        """
        try:
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            # creating folder
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)
            dataframe.to_csv(feature_store_file_path, index=False, header=True)
            return dataframe

        except Exception as e:
            raise NetworkSecurityException(e, sys.exc_info()) from e
        
    def split_data_as_train_test(self, dataframe: pd.DataFrame):
        """
        Method Name :   split_data_as_train_test
        Description :   This method splits the DataFrame into train and test sets.

        Output      :   train_set_path, test_set_path
        On Failure  :   Raise Exception
        """
        try:
            if dataframe.empty or len(dataframe) == 0:
                raise Exception(
                    "Cannot split empty dataframe. Please check MongoDB collection has data."
                )
            
            logging.info(f"Splitting {len(dataframe)} records into train and test sets")
            train_set, test_set = train_test_split(dataframe, test_size=0.2, random_state=42)
            logging.info("Performed train test split on the dataset")
            # creating dataset directory
            dataset_dir = os.path.dirname(self.data_ingestion_config.train_file_path)
            os.makedirs(dataset_dir, exist_ok=True)
            logging.info("Created dataset directory")
            train_set.to_csv(self.data_ingestion_config.train_file_path, index=False, header=True)
            test_set.to_csv(self.data_ingestion_config.test_file_path, index=False, header=True)
            logging.info("Exported train and test file")

        except Exception as e:
            raise NetworkSecurityException(e, sys.exc_info()) from e

    def initiate_data_ingestion(self):
        try:
            dataframe = self.export_collection_as_dataframe()
            dataframe = self.export_data_into_feature_store(dataframe)
            self.split_data_as_train_test(dataframe)
            dataingestionartifact = DataIngestionArtifact(
                trained_file_path=self.data_ingestion_config.train_file_path,
                test_file_path=self.data_ingestion_config.test_file_path
            )
            return dataingestionartifact
        except Exception as e:
                raise NetworkSecurityException(e, sys.exc_info()) from e
