from flask import Flask, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask_cors import CORS
import requests
from models import Base, User, Business, Comment, BusinessComment
from sqlalchemy.orm import sessionmaker
import requests
import csv
import json

def main():
    app = Flask(__name__)
    db = SQLAlchemy(app)
    engine_options = app.config['SQLALCHEMY_ENGINE_OPTIONS']

    engine = db.create_engine('postgresql+psycopg2://postgres:swimmeet@localhost/covid_business', engine_options)
    #Base.metadata.drop_all(engine) #DO NOT UNCOMMENT UNLESS DEVELOPING
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

if __name__ == '__main__':
    main()