from flask import request,jsonify
from db import db

users = db["users"]

def register_user():

    data=request.get_json()

    user={
        "name":data["name"],
        "email":data["email"],
        "points":0,
        "streak":0
    }

    users.insert_one(user)

    return jsonify({"message":"User Added"})