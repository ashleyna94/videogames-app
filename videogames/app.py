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
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///"
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


# Create route that renders html templates
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/mosaic.html")
def mosaic():
    return render_template("mosaic.html")

@app.route("/trends.html")
def trends():
    return render_template("trends.html")

@app.route("/topsales.html")
def genres():
    return render_template("topsales.html")

@app.route("/gamecount.html")
def publishers():
    return render_template("gamecount.html")

@app.route("/machine_learning.html")
def machine_learning():
    return render_template("machine_learning.html")

def get_dict_of_data(df, colname):
    column_dict = df[colname].value_counts().astype(float).to_frame().to_dict(orient="split")
    column_dict["data"] = [x[0] for x in column_dict["data"]]
    return column_dict

@app.route("/api/plot")
def returntable():
    stmt = session.query(Videogames).statement

    # #Game Count 
    df = pd.read_sql_query(stmt, session.bind)
    df_filter = df.head()
    # df = df[['Name','Platform']].groupby(['Platform']).count().sort_values('Name', ascending=False).reset_index
    columns_to_count = ["Platform", "Genre", "Publisher"]

    column_counts = {colname: get_dict_of_data(df, colname) for colname in columns_to_count}
    json_for_plotly = jsonify(column_counts)
    return json_for_plotly


@app.route("/api/genre")
def genre():
    stmt = session.query(Videogames).statement
    df = pd.read_sql_query(stmt, session.bind)
    genre_list = list(df["Genre"].unique())

    return jsonify(genre_list)

if __name__ == "__main__":
    app.run()
