from flask import request,jsonify
from db import db

challenges=db["challenges"]

def create_challenge():

    data=request.get_json()

    challenge={
        "title":data["title"],
        "duration":data["duration"],
        "participants":[]
    }

    challenges.insert_one(challenge)

    return jsonify({"message":"Challenge Created"})