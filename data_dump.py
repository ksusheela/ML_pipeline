import pandas as pd
import os, sys
import pymongo
import json
from schema import write_Schema_yaml
#from pathlib import Path
#from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://purnima11:Pavanpabba629@cluster0.twh81ir.mongodb.net/?retryWrites=true&w=majority"

DATA_FILE_PATH = open(r"C:\\ML_pipeline\\data\\train.csv")
DATABASE = "Machine_learning"
COLLECTION_NAME = "DATASET"


if __name__ == "__main__":

    ROOT_DIR =os.getcwd()

    DATA_FILE_PATH = os.path.join(ROOT_DIR,'data','train.csv')

    FILE_PATH = os.path.join(ROOT_DIR, DATA_FILE_PATH)

    write_Schema_yaml(csv_file = DATA_FILE_PATH)

    df = pd.read_csv(DATA_FILE_PATH)

    print(f"Rows and Columns of our Data: {df.shape}")

    #df.reset_index(drop = True, inplace = True)

    
    # convert the dataframe to a lst of dictionaries(json records)
    json_records = json.loads(df.to_json(orient="records")) 
    print(json_records[0])

#esrablish aconnection to mangoDB
    client = pymongo.MongoClient(uri)

# Access the desired database and collection
    db = client[DATABASE]
    collection = db[COLLECTION_NAME]

# Insert  the Json records into the collection
    collection.insert_many(json_records)

    # Close the mongoDB connection
    client.close()