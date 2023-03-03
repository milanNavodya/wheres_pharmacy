from config import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    # Common fields for user
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(200))
    email = db.Column(db.String(40), unique=True)
    password = db.Column(db.String(100))
    gender = db.Column(db.String(20))
    dob = db.Column(db.DateTime)
    address = db.Column(db.String(100))
    mobile = db.Column(db.String(20))
    user_type = db.Column(db.String(20))

    # For doctor type users
    # position = db.Column(db.String(100))
    # category = db.Column(db.String(100))

    def __init__(self, name, email, password, gender, dob, address, mobile, user_type):
        self.full_name = name
        self.email = email
        self.password = password
        self.gender = gender
        self.dob = dob
        self.address = address
        self.mobile = mobile
        self.user_type = user_type
        # For Doctor
        # self.position = position
        # self.category = category
