# flask_app.py
from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/julia")
def hello_from_julia():
    return "Hello From Julia!"


@app.route('/hello/<username>')
def greet_username(username):
    return 'Hello %s' % username


@app.route('/about')
def about():
    return 'The about page'


@app.route('/api')
def api():
    data = {
        'name': 'Fleabag',
        'year': '2019',
        'watched': 'yesterday',
        'similar_to': 'Killing_Eve'
    }

    return jsonify(data)


@app.route('/pandas')
def pandas_api():

    data = {'name': ['Fleabag', 'Killing_Eve', 'Dr Who'], 'some_numbers': [3, 4, 12]}

    pandas_data = pd.DataFrame(data=data)

    return pandas_data.to_json()
