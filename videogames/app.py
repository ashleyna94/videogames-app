# Import necessary libraries
import os
import numpy as np
import pandas as pd
from datetime import datetime
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import (
    Flask, render_template, jsonify,
    request, redirect)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URL'] = os.environ.get('DATABASE_URL', '') or "sqlite:///video_games.sqlite"
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '')
db = SQLAlchemy(app)

# from .models import Videogames


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///video_games.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)

Videogames = Base.classes.videogames
session = Session(engine)


# Create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/genre")
def genre():
    stmt = session.query(Videogames).statement
    df = pd.read_sql_query(stmt, session.bind)
    genre_list = list(df["Genre"].unique())

    return jsonify(genre_list)

if __name__ == "__main__":
    app.run()
