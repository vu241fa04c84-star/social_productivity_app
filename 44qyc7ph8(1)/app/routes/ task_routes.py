from flask import Blueprint
from app.controllers.task_controller import add_task

task_bp=Blueprint("task",__name__)

task_bp.route("/add",methods=["POST"])(add_task)