import csv
from src.dal.db_connect import MongoDB

class LoadData():
    """
    docstring
    """
    def __init__(self, path_file):

        self.path_file = path_file
        self.dict_list = []
    

    def csv_to_dict(self):

        with open (self.path_file, 'r') as f:
            reader = csv.DictReader(f)
            for line in reader:
                self.dict_list.append(line)
        return self.dict_list

    def insert_csv(self, con = MongoDB('user_name', 'password', 'db_name', 'collection_name')):

        self.csv_to_dict()

        _, self.collection_mdb = con.__connect__()
        self.collection_mdb.insert_many(self.dict_list, ordered = False)
        print("All the countries data has been Exported to Mongo db server")









        

