from flask import jsonify,request
from httpproblem import problem
from functools import wraps
import os

def require_appkey(view_function):
    @wraps(view_function)

    # the new, post-decoration function. Note *args and **kwargs here.
    def decorated_function(*args, **kwargs):
        
        api_key = "b4fe4ccd-99c2-a129-f0a8-c555cb4724d2"

        # if request.args.get('key') and request.args.get('key') == key:
        if (request.headers.get("api-key") and 
            request.headers.get("api-key") == api_key):
            return view_function(*args, **kwargs)
        else:
            return (
                jsonify(
                    problem(401, "Unauthorized", "Unauthorized access", request.path)
                ),
                401,
            )

    return decorated_function