from src.upload_data.load_data import LoadData
from src.dal.db_connect import MongoDB

# MongoDB authentification 

user_name = 'Admin'
password = 'denied87ZONE8787'
db_name = 'country_db'
collections_name = 'country_records'

# Dataset path
dataset_path = 'data/countries_cleaned.csv'

# MongoDB connection 
con = MongoDB(user_name, password, db_name , collections_name)

#
ld = LoadData(dataset_path)

# Uploadind Data to MongoDB cluster (Azure)
ld.insert_csv(con)








