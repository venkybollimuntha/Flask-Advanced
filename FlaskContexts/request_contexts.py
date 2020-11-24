# Request context (request, session)

# request ---> with app.test_request_context('/'):
# session ---> with app.test_request_context('/'):


from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    print(request)
    return "something"

# it seems that request object is global, buts its really not

# If you want to access the request object outside the view function

# print(request.method) # This will raise RuntimeError: Working outside of request context.

# if you want to access request object out side function you have to create request context.

# request_context case1: accessing request object out side view funtion
request_ctx = app.test_request_context()
request_ctx.push()
request.method

#request_context case2: accessing request object out side view funtion
with app.test_request_context('/'):
    print(request.method)

