from user_feedback import db

class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(250), nullable=False)
    date_of_birth = db.Column('date_of_birth', db.Date, nullable=False)
    email = db.Column('email',db.String(250), nullable=False)
    country = db.Column('country',db.String(250), nullable=False)
    city = db.Column('city',db.String(250), nullable=False)
    likes = db.Column('likes',db.String(250), nullable=False)
    dislikes = db.Column('dislikes',db.String(250), nullable=False)

    @property
    def serialized(self):
        return {
            'id': self.id,
            'name': self.name,
            'date_of_birth': self.date_of_birth,
            'email': self.email,
            'country': self.country,
            'city': self.city,
            'likes': self.likes,
            'dislikes': self.dislikes,
        }