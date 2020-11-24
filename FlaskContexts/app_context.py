# Application context (current_app, g)

# current_app --> with app.app_context()
# g ---> app.test_request_context('/')

from flask import Flask, g
app = Flask(__name__)
with app.app_context():
    g.my_db = 'database ok'
    print(g.my_db)


# but if you try to access outside the app_context raise an error

print(g.my_db)

# Even if you create new context, it will throw the same error

with app.app_context():
    print(g.my_db)


## current_app context example ##

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_redis import FlaskRedis
def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    # Set globals
    db = SQLAlchemy()
    redis_store = FlaskRedis()
    with app.app_context():
        # Set global values
        redis_store.endpoint = app.config['ENDPOINT']
        redis_store.post_query = app.config['POST_QUERY']
        
        # Initialize globals
        redis_store.init_app(app)
        db.init_app(app)
        # Add some routes
        from . import routes
return app


# routes.py
from flask import current_app as app
from flask import make_response
import json
from . import models
from . import redis_store
headers = { 'Access-Control-Allow-Headers': 'Content-Type' }
@app.route('/', methods=['GET', 'POST'])
def entry():
    readers = models.Readers.query.filter_by(username='john').all()
    print(readers)
    print(redis_store.endpoint)
    return make_response(str('readers'), 200, headers)
