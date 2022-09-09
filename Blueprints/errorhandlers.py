from flask import jsonify
from httpproblem import problem

def handle_404(e):
    error = str(e)
    # return jsonify({"error": "Bad Request", "message": error}), 404
    return (
        jsonify(problem(404, "Not Found", error)),
        404,
    )


class NotFoundError(Exception):
    def __init__(self, message, request):
        self.message = message
        self.request = request

        
# Another way of handling error
def handle_not_found_error(ee: NotFoundError):
    return (
        jsonify(
            problem(
                404,
                "Not Found",
                ee.message,
                ee.request.path,
            )
        ),
        404,
    )