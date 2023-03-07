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
    user_role = db.Column(db.String(20))

    # For doctor type users
    position = db.Column(db.String(100))
    category = db.Column(db.String(100))

    # For Pharmacist
    pharmacy_reg_no = db.Column(db.String(100))

    secret_key = db.Column(db.String)

    def __init__(self, full_name, email, password, gender, dob, address, mobile, user_role, position, category,
                 pharmacy_reg_no, secret_key):
        self.full_name = full_name
        self.email = email
        self.password = password
        self.gender = gender
        self.dob = dob
        self.address = address
        self.mobile = mobile
        self.user_role = user_role
        # For Doctor
        self.position = position
        self.category = category
        # For Pharmacist
        self.pharmacy_reg_no = pharmacy_reg_no
        self.secret_key = secret_key


class Product(UserMixin, db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    unit = db.Column(db.String)


class ProductStock(UserMixin, db.Model):
    __tablename__ = 'product_stock'
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Double)
    product_id = db.Column(db.Integer)
    pharmacy_id = db.Column(db.Integer)

    def __init__(self, quantity, price, product_id, pharmacy_id):
        self.quantity = quantity
        self.price = price
        self.product_id = product_id
        self.pharmacy_id = pharmacy_id
