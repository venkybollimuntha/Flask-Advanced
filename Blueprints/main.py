from flask import Flask 
from bp_1 import tree_mold
from bp_2 import venky
from errorhandlers import handle_404,handle_not_found_error,NotFoundError
from extensions import extend_headers


# Initializing the application
app = Flask(__name__)


# Initializing extended headers
# we can use flask_extend_headers for API versioning
app.config["EXTEND_HEADERS_KEY"] = "accept-version"
extend_headers.init_app(app)


# Registering the blue prints 
app.register_blueprint(venky, url_prefix="/venky")
app.register_blueprint(tree_mold)


# Register Error handlers
app.errorhandler(404)(handle_404)
app.errorhandler(NotFoundError)(handle_not_found_error)



if __name__ =="__main__":
	app.run(debug=True)
