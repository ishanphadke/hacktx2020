from flask import Flask, render_template
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager
import json

app = Flask("__main__")
CORS(app)

@app.route("/business")
def business():
    return json.dumps({'name': 'alice',
                       'email': 'alice@outlook.com'})

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:swimmeeet@localhost/covid_business'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.run(debug=True)
