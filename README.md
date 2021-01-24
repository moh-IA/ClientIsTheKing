# ClientIsTheKing
 ### Description 
 The goal of this project is to manipulate the data of world countries with NoSQL concept, for that i have used *Atlas MongoDB cloud* data base.
 To request this database an API has been created with Flask framework.
 
 ### Using the API
 To request database on *Atlas MongoDB* and getting results, frist you should clone the repo of [project](https://github.com/moh-IA/ClientIsTheKing.git) and run the file [app.py](https://github.com/moh-IA/ClientIsTheKing/blob/main/app.py).  
 Once the server is running click on:  http://localhost:8080/.    
 
 1. find_country() function: Return the informations of country, it takes name of country as parameter:
   ```Python 
       @app.route('/find_country/<name_country>')
       def find_country(name_country):
          country = records.find_one({'name_country': name_country})
          del country['_id']

          return country 
  ```
   Example: http://localhost:8080/find_country/France.
     
2. add_country() function: Add new country to the collection as a new document,it takes name of country as parameter:  
  ```Python
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
   ```
   Example: http://localhost:8080/add_country/Marseille.  
   
     
3. get_desnity_tranch() function: Return the tranche density of country, it takes name of country as parameter.  
  ```Python
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
  ```  
  Example: http://localhost:8080/get_tranch/Marseille.  
  
4. Set the date of insert during creation of new country or update date of midification whene value field changed:   
   For that i have created two Triggers on Atlas one after INSERT operation and another after UPDATE operation.
   ```node.js
      exports = function(changeEvent) {
        const collection = context.services.get('Cluster0').db("country_db").collection("country_records");
        collection
        .updateOne(
           { _id: changeEvent.documentKey._id },
           { $set: { date_creat: new Date() } }
         )
             

        return;
     };
   ```
 Example: for example if we want to update density of a country 
 http://localhost:8080/update_country/Bordeaux/200.
 
```node.js
   {
   _id:600db05146a7626ae5e74e86
    name_country:"Bordeaux"
    population:"252046173.66"
    yearly_change:"-0.19"
    net_change:"9794282.01"
    density:"200"
    land_area:"12266271.33"
    migrants_net:"-194022.08"
    fert_rate:"5.50"
    med_age:"17.27"
    urban_pop:"35.0"
    world_share:"7.29"
    date_creat:2021-01-24T17:37:21.862+00:00
    date_modif:2021-01-24T17:38:51.601+00:00
  }
```
 
 
 
