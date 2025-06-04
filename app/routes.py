from flask import Blueprint, request
from .utils import url_shortener

url_blueprint = Blueprint("url_shortener", __name__)

@url_blueprint.route("/")
def hello():
    return "Hello World"

@url_blueprint.route("/identify", methods=["POST"])
def shorten():
    data = request.get_json()
    return url_shortener(data)
