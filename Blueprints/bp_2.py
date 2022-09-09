from flask import Blueprint
from extensions import extend_headers, #db
from flask_cors import cross_origin
from decorator_helpers import require_appkey


venky = Blueprint("venky", __name__)

def one_version():
    return "Calling one one_version"


# If you include header Accept-Version : application/v1 then your request is routed to one_version
# otherwise request is routed to one function

# Decoration order of execution is top to bottom. so be careful when you decorate the function
# first priority is path then auth then extend headers

@venky.route("/one")
@require_appkey
@extend_headers.register(extensions={"application/v1": one_version})
@cross_origin(headers=["Content-Type", "Authorization"])
def one():
    return "Directly calling one version"

@cross_origin(headers=["Content-Type", "Authorization"])
@venky.route("/hands")
@require_appkey
def leaves():
    return "Venky has hands"


@venky.route("/legs")
@require_appkey
def roots():
    return "Venky has legs as well"

#@venky.route('/dbcheck')
#@require_appkey
# def db_method():
#     account = Account.query.filter(Account.request_id == id,).first()
#     account.name ="venkyBollimuntha"
#     db.session.add(account)
#     db.session.commit()