from src.upload_data.load_data import LoadData
from src.dal.db_connect import MongoDB
from flask import Flask, render_template, url_for
from flask import request, jsonify
import json
import random



# MongoDB authentification

user_name = 'Admin'
password = 'denied87ZONE8787'
db_name = 'country_db'
collections_name = 'country_records'

# Dataset path
dataset_path = 'data/countries_cleaned.csv'

# MongoDB connection
con = MongoDB(user_name, password, db_name, collections_name)
_, records = con.connect()
ld = LoadData(dataset_path)


app = Flask(__name__)

# Uploadind Data to MongoDB cluster (Azure)


@app.route('/load_data')
def loading_data():
    ld.insert_csv(con)

# Get country
@app.route('/')
def index():
    return "The client is the King"

@app.route('/find_country/<name_country>')
def find_country(name_country):
    country = records.find_one({'name_country': name_country})
    del country['_id']

    return country

# Add country


@app.route('/add_country/<name_country>/')
def add_country(name_country):

    new_country = {
        'name_country': name_country,
        'population': str(round(random.uniform(801, 1438207241), 2)),
        'yearly_change': str(round(random.uniform(-2.47, 3.84), 2)),
        'net_change': str(round(random.uniform(-383840, 13586631), 2)),
        'density': str(round(random.uniform(0, 26337), 2)),
        'land_area': str(round(random.uniform(0, 16376870), 2)),
        'migrants_net': str(round(random.uniform(-653249.00, 954806.00), 2)),
        'fert_rate': str(round(random.uniform(1.10, 7), 2)),
        'med_age': str(round(random.uniform(15, 48), 2)),
        'urban_pop': str(round(random.uniform(0, 100), 2)),
        'world_share': str(round(random.uniform(0, 18.47), 2)),
        'date_creat': "",
        'date_modif': ""

    }

    records.insert_one(new_country) 
    return f"the new country { name_country } has been added successfully"

# Modify density field to check date_modif


@app.route('/update_country/<name_country>/<density>')
def update_country(name_country, density):

    records.update_one({"name_country": name_country},
                       {"$set": {"density": density}})

    return f"the Density of { name_country } has been modified"

# Return the tranch of density


@app.route('/get_tranch/<name_country>')
def get_density_tranch(name_country):

    country = records.find_one({'name_country': name_country})
    density = int(country['density'])
    if density <= 100:
        return f'{name_country} with density equal to : { density } is in the tranche: T1 0-100'
    elif density > 100 and density <= 1000:
        return f'{name_country} with density equal to : { density }  is in the tranche: T2 101-1000'
    elif density > 1000 and density <= 10000:
        return f'{name_country} with density equal to : { density }  is in the tranche: T3 1001-10000'
    else:
        return f'{name_country} with density equal to : { density }  is in the tranche: T4 more than 10000'


if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)
