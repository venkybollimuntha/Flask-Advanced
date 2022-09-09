# we can use flask_extend_headers for API versioning
# use it as a decorator
# Return with different views based on the custom header you set

from flask_extend_headers import ExtendHeaders
# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
# from flask_limiter import Limiter
# from flask_limiter.util import get_ipaddr
# from flask_extend_headers import ExtendHeaders
# db = SQLAlchemy()

extend_headers = ExtendHeaders()


