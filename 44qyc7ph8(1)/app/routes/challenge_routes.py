from flask import Blueprint
from app.controllers.challenge_controller import create_challenge

challenge_bp=Blueprint("challenge",__name__)

challenge_bp.route("/create",methods=["POST"])(create_challenge)