import pandas as pd
import pymongo
import json
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://purnima11:Pavanpabba629@cluster0.twh81ir.mongodb.net/?retryWrites=true&w=majority"


DATA_FILE_PATH = (r"C:\\ML_pipeline\\data\\train.csv")
DATABASE = "Machine_learning"
COLLECTION_NAME = "DATASET"

if __name__ =="__main__": 

# read the data from theCSV file into a pandas Dataframe    
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns:{df.shape}")

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