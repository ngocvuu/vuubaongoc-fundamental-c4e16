from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)

db = client.get_default_database()

posts = db["posts"]

new_post = {
    "title": "Làm Gì Sau Khi Code",
    "author":"Khánh Linh",
    "content": """
        1. Xem Phim Hàn
        2. Xem lại Code
        3. Làm Bài Tập
        Châm ngôn: Code, code nữa, code mãi
    """
}

posts.insert_one(new_post)
