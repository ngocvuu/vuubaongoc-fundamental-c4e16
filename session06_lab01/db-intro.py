from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds117539.mlab.com:17539/c4e16-lab"

#1. Connect to database
client = MongoClient(mongo_uri)

#2. Get database
db = client.get_default_database()

#3. Create Collection
games = db["games"]
blogs = db["blogs"]
# #4. Create a new document
# new_game = {
#     "name" : "Hứng bia",
#     "description": "Best game ever"
# }
#
#
# new_blog = {
#     "name" : "The Present Writer",
#     "description" : "everything"
# }
#
# #5. Insert document into collection
# games.insert_one(new_game)
# blogs.insert_one(new_blog)

all_game = games.find()

for game in all_game:
    print(game["name"])
