from flask import request,jsonify
from db import db

tasks=db["tasks"]

def add_task():

    data=request.get_json()

    task={
        "user":data["user"],
        "task":data["task"],
        "status":"pending"
    }

    tasks.insert_one(task)

    return jsonify({"message":"Task Added"})