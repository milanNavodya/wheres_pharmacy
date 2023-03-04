from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from flask_login import login_user, logout_user, login_required
from config import db

routes = Blueprint('routes', __name__)  # Blueprint object for routes


@routes.route('/login', methods=['GET', 'POST'])  # path for login page
def login():  # define login page function
    if request.method == 'GET':  # if the request is a GET we return the login page
        return render_template('login.html')
    else:  # if the request is POST then we check if the user exist and with te right password
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember-me') else False
        user = User.query.filter_by(email=email).first()  # check if the user actually exists
        # take the user-supplied password, hash it, and compare it to the hashed password in the database

        if not user:
            flash('Please sign up before!')
            return redirect(url_for('views.user_type'))
        elif not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('routes.login'))  # if the user doesn't exist or password is wrong, reload the page
        # if the above check passes, then we know the user has the right credential's
        session['id'] = user.id

        login_user(user, remember=remember)
        if user.user_role == 'patient':
            return redirect(url_for('views.index_user'))
        elif user.user_role == 'doctor':
            return redirect(url_for('views.index_doctor'))
        elif user.user_role == 'pharmacist':
            return redirect(url_for(''))
        else:
            return redirect(url_for('views.user_type'))


@routes.route('/signup', methods=['GET', 'POST'])  # we define the sign up path
def signup():  # define the signup function
    if request.method == 'GET':  # If the request is GET we return the sign up page and forms
        return render_template('signup.html')
    else:  # if the request is POST, then we check if the email doesn't already exist and then we save data
        name = request.form.get('fullname')
        email = request.form.get('email')
        password = request.form.get('password')
        gender = request.form.get('gender')
        dob = request.form.get('dob')
        street = request.form.get('street')
        city = request.form.get('city')
        state = request.form.get('state')
        county = request.form.get('county')
        address = street + ", " + city + ", " + state + ", " + county + "."
        mobile = request.form.get('mobile')
        user_type = "patient"
        # For Doctor registration
        position = request.form.get('position')
        category = request.form.get('category')
        # For Pharmacist Registration
        pharmacy_reg_no = request.form.get('pharmacy_reg_no')
        if position and category:
            user_type = "doctor"
        if pharmacy_reg_no:
            user_type = "pharmacist"

        user = User.query.filter_by(email=email).first()  # return user if email already exist
        if user:  # if that user already registered return again to sign up page
            flash('Email address already exists.')
            return redirect(url_for('routes.signup'))

        # create a new user with the form data. Hash the password so the plaintext version isn't saved.
        new_user = User(full_name=name, email=email, password=generate_password_hash(password), gender=gender, dob=dob,
                        address=address, mobile=mobile, position=position, category=category,
                        pharmacy_reg_no=pharmacy_reg_no, user_role=user_type)
        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('routes.login'))


@routes.route('/logout', methods=['POST'])  # path for logout
@login_required
def logout():  # function for logout action
    logout_user()
    return redirect(url_for('views.index'))


@routes.route('/index')
def index():
    return redirect(url_for('views.index'))
