# Create a Postgresql database to hold Cannabis data
# Completed and working, credentials saved in .env file

# Imports
import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values
import json
import pandas
import numpy as np

# Load credentials
load_dotenv()

# Postgresql credentials from .env file
db_name = os.getenv('DB_name', default= 'OOPS')
db_user = os.getenv('DB_user', default= 'OOPS')
db_pwd = os.getenv('DB_pwd', default= 'OOPS')
db_host = os.getenv('DB_host', default= 'OOPS')


# Connect to ElephantSQL-hosted PostgreSQL
connection = psycopg2.connect(dbname=db_name, user=db_user,
                        password=db_pwd, host=db_host)
print(type(connection))


# Create cursor to perform queries
cursor = connection.cursor()
print(type(cursor))



# # # Design table
# table_creation_query = '''
# CREATE TABLE IF NOT EXISTS Cannabis (
#     strain_id SERIAL PRIMARY KEY,
#     strain_name varchar(100),
#     strain_type varchar(10),
#     strain_rating INTEGER,
#     effects_profile varchar(8000),
#     flavor_profile varchar(8000),
#     strain_description varchar(8000),
#     strain_profile varchar(8000)
# )
# '''

# # Create table
# cursor.execute(table_creation_query)


# ## INSERT DATA IN THE TABLE

# # Read CSV and save as df
# CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "med_cabinet_cleaned.csv")
# df = pandas.read_csv(CSV_FILEPATH)

# # df.index += 1 # to start index at 1 (resembling primary key behavior)
# df.drop('Unnamed: 0', axis= 1, inplace=True)
# print(df.head())

# psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)

# # Convert dataframe to tuples
# list_of_tuples = list(df.to_records(index=False))


# # Insert Data from Cannabis csv
# insertion_query = "INSERT INTO Cannabis_2 (strain_id, strain_name, strain_type, strain_rating, effects_profile, flavor_profile, strain_description, strain_profile) VALUES %s"
# execute_values(cursor, insertion_query, list_of_tuples)


# # Save the transaction - commit changes to PostgreSQL site
# connection.commit()
# cursor.close()
# connection.close()
