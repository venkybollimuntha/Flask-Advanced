from flask import Flask 
from bp_1 import tree_mold
from bp_2 import venky

app = Flask(__name__)

app.register_blueprint(venky, url_prefix="/venky")
app.register_blueprint(tree_mold, url_prefix="/oak")
app.register_blueprint(tree_mold, url_prefix="/fir")
app.register_blueprint(tree_mold, url_prefix="/ash")


app.run(debug=True)