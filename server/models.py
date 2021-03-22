from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

db = SQLAlchemy()

class FeedbackModel(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  birth_date = db.Column(db.Date(), nullable=False)
  email_address = db.Column(db.String(200), nullable=False)
  country = db.Column(db.String(150), nullable=False)
  city = db.Column(db.String(200), nullable=False)
  created_on = db.Column(db.DateTime(), default=datetime.utcnow)
  good_comment = db.Column(db.String(500), nullable=False)
  bad_comment = db.Column(db.String(500), nullable=False)
  
  def __repr__(self):
    return self.name


