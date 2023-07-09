import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request

# Get values from environment variables
load_dotenv()
url = os.getenv("DATABASE_URL")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = url
db = SQLAlchemy(app)

# We import routes and models
from app import models, routes