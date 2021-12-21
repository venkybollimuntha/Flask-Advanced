from flask import Blueprint

venky = Blueprint("venky", __name__)

@venky.route("/hands")
def leaves():
    return "Venky has hands"

@venky.route("/legs")
def roots():
    return "Venky has legs as well"
