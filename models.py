from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class TransportMode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mode = db.Column(db.String(50), nullable=False)
    cost_per_mile = db.Column(db.Float, nullable=False)
    time_per_mile = db.Column(db.Float, nullable=False)
    emissions_per_mile = db.Column(db.Float, nullable=False)
