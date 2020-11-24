from flask import Flask
from flask.views import View,MethodView

app = Flask(__name__)


class MyClass(View):

    # name must be dispatch_request, other wise gives NotImplemented error

    # By default, only dispatch_request is called.

    def dispatch_request(self):

        x = self.internal_method()
        return x

    def internal_method(self):
        return 20

class SecondClass(MethodView):

# By passing MethodView, we can use syntax like Django classes.
# get, post, put, delete.... etc
    def get(self):
        return "hey working"

    def post(self):
        return "hey post method"



app.add_url_rule("/first", view_func=MyClass.as_view("first"))
app.add_url_rule("/second",view_func= SecondClass.as_view("second"),methods=['GET','POST'])

# as_view(MUST_BE_UNIQUE_NAME)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
