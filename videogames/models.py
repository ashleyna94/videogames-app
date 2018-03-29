from .app import db

class Videogames(db.Model):
    __tablename__ = 'videogames'

    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.Text)
    Platform = db.Column(db.Text)
    Year_of_Release = db.Column(db.Integer)
    Genre = db.Column(db.Text)
    Publisher = db.Column(db.Text)
    NA_Sales = db.Column(db.Float)
    EU_Sales = db.Column(db.Float)
    JP_Sales = db.Column(db.Float)
    Other_Sales = db.Column(db.Float)
    Global_Sales = db.Column(db.Float)
    Critic_Score = db.Column(db.Integer)
    Critic_Count = db.Column(db.Integer)
    User_Score = db.Column(db.Float)
    User_Count = db.Column(db.Integer)
    Rating = db.Column(db.Text)

    def __repr__(self):
        return '<Video Game %r>' % (self.name)
