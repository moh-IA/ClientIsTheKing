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
    









