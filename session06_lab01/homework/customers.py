from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)

db = client.get_default_database()

customers = db["customers"]

total_numb = customers.find()

events_count = 0
ads_count = 0
wom_count = 0

for key in total_numb:
    if key["ref"] == "events":
        events_count += 1
    elif key["ref"] == "ads":
        ads_count += 1
    elif key["ref"] == "wom":
        wom_count += 1

print("Total number of customers by group: ","events: ", events_count, ", ads: ", ads_count, ", wom : ", wom_count)
