# we can use flask_extend_headers for API versioning
# use it as a decorator
# Return with different views based on the custom header you set

from flask_extend_headers import ExtendHeaders


extend_headers = ExtendHeaders()

