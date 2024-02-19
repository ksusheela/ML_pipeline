#import yaml
import yaml
import os, sys
import os.path
import pandas as pd

def write_Schema_yaml(csv_file):
    df=pd.read_csv(csv_file)

    num_cols = len(df.columns)

    columns_names = df.columns.tolist()

    column_dtype =df.dtypes.astype(str).tolist()
    
    #create schema dictonary

    schema = {
        "filename":os.path.basename(csv_file),
        "NumberofColumns": num_cols,
        "ColumnName":dict(zip(columns_names,column_dtype))
    }

    # write schema to schema.yaml file

    ROOT_DIR = os.getcwd()
    SCHEMA_PATH = os.path.join(ROOT_DIR, 'config' 'schema.yaml')

    with open(SCHEMA_PATH, 'w') as file:
        yaml.dump(schema,file)