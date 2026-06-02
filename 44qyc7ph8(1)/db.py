from pymongo import MongoClient

client = MongoClient('mongodb+srv://vu241fa04c84_db_user:8978787959@cluster0.rqphorj.mongodb.net/?appName=Cluster0')

db = client["productivity_app"]