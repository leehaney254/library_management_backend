from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:7711@localhost/libraryManagement'
db = SQLAlchemy(app)

# We import routes and models
from app import models, routes