from pymongo import MongoClient

db_url = 'mongodb+srv://ducminh123:ndm30122005@duckling.073kz.mongodb.net/?retryWrites=true&w=majority'
myclient = MongoClient(db_url)

mydb = myclient["db-test"]
mycol = mydb["py-collection"]

# print(mydb.list_collection_names())

mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict)

# print(x.inserted_id)

mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]
x = mycol.insert_many(mylist)

# for i in x.inserted_ids:
#     print(i)

x = mycol.find_one()
# print(x)

# for x in mycol.find({},{ "name": 1, "_id": 0 }):
#   print(x)

myquery = { "address": "Park Lane 38"}
mydoc = mycol.find_one(myquery)
# print(x)

myquery = { "address": { "$gt": "S" }}
mydoc = mycol.find(myquery)

# for x in mydoc:
#     print(x)

mydoc = mycol.find().sort('name')
# print(mydoc[0])

myquery = { "address": "Mountain 21" }
# x = mycol.delete_one(myquery)

myquery = { "name": {"$lt": "B"}}
# x = mycol.delete_many(myquery)

# print(x.deleted_count, " documents deleted.")

myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }

mycol.update_many(myquery, newvalues)

# for x in mycol.find({"address": "Canyon 123"}):
#     print(x)

myresult = mycol.find().limit(5)
for x in myresult:
    print(x)