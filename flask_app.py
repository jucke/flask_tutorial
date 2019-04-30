# flask_app.py
from flask import Flask
app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/julia")
def hello_from_julia():
    return "Hello From Julia!"

@app.route('/hello/<username>')
def show_user_profile(username):
    return 'Hello %s' % username
