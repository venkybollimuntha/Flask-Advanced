# Reference link https://testdriven.io/courses/python-web-framework/wsgi/


1. Web server : (Apache, Nginx,etc..)

2. WSGI server (gunicorn / uWSGI / mod_wsgi)

    WSGI, which stands for Web Server Gateway Interface,
    is an interface between a web server and a Python-based web application. 
    It is required since a web server cannot talk directly to a Python application. 

    Note: (WSGI servers are language specific)
    for Ruby ----> rack
    for Python ---> WSGI (pronounce as WIZ-ghee)
    for Java -----> Servlets 



3. Flask application.


from wsgiref.simple_server import make_server


class Reverseware:
    def __init__(self, app):
        self.wrapped_app = app

    def __call__(self, environ, start_response, *args, **kwargs):
        wrapped_app_response = self.wrapped_app(environ, start_response)
        return [data[::-1] for data in wrapped_app_response]


def application(environ, start_response):
    response_body = [
        f'{key}: {value}' for key, value in sorted(environ.items())
    ]
    response_body = '\n'.join(response_body)

    status = '200 OK'

    response_headers = [
        ('Content-type', 'text/plain'),
    ]

    start_response(status, response_headers)

    return [response_body.encode('utf-8')]


server = make_server('localhost', 8000, app=Reverseware(application))
server.serve_forever()
