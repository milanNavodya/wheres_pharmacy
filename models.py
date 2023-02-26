from config import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    # Common fields for user
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(40), unique=True)
    name = db.Column(db.String(200))
    street = db.Column(db.String(100))
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    county = db.Column(db.String(100))
    mobile = db.Column(db.String(20))
    user_type = db.Column(db.String(20))

    # For doctor type users
    position = db.Column(db.String(100))
    category = db.Column(db.String(100))

    def __init__(self, email, name, street, city, state, county, mobile, user_type, position, category):
        self.email = email
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.county = county
        self.mobile = mobile
        self.user_type = user_type
        self.position = position
        self.category = category
