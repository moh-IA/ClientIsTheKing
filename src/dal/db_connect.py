from pymongo import MongoClient



class MongoDB():
    """
    docstring
    """
    def __init__(self, user_name, password, db_name, collection_name):

        self.user_name = user_name
        self.password = password
        self.db_name = db_name
        self.collection_name = collection_name

    
    def connect(self):

        self.client = MongoClient(f"mongodb+srv://{self.user_name}:{self.password}@cluster0.hdjon.mongodb.net/{self.db_name}?retryWrites=true&w=majority")
        self.db = self.client[self.db_name]
        self.collection = self.db[self.collection_name]

        return self.db, self.collection
    




# MongoDB authentification

user_name = 'Admin'
password = 'denied87ZONE8787'
db_name = 'country_db'
collections_name = 'country_records'



# MongoDB connection
con = MongoDB(user_name, password, db_name, collections_name)
_, records = con.connect()

records.update_one({"name_country": "Bordeaux"}, {"$set": {"fert_rate": "5.50"}})







