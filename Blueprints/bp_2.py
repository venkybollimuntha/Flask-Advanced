from flask import Blueprint
from extensions import extend_headers
from flask_cors import cross_origin



venky = Blueprint("venky", __name__)

def one_version():
    return "Calling one one_version"



# If you include header Accept-Version : application/v1 then your request is routed to one_version
# otherwise request is routed to one function
@venky.route("/one")
@extend_headers.register(extensions={"application/v1": one_version})
def one():
    return "Directly calling one version"

@cross_origin(headers=["Content-Type", "Authorization"])
@venky.route("/hands")
def leaves():
    return "Venky has hands"

@venky.route("/legs")
def roots():
    return "Venky has legs as well"