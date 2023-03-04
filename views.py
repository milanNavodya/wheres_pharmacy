from flask import Blueprint, render_template, request, flash, jsonify, session, redirect, url_for
from flask_login import login_required
from config import db
from datetime import datetime
import routes

views = Blueprint('views', __name__)


@views.route('/')
# login page that return 'login'
def index():
    return render_template('index.html')


@views.route('/user-type')
# user can select user type in this page
def user_type():
    return render_template('account_type.html')


@views.route('/signup-doc')
# Return view for normal user
def signup_doctor():
    return render_template('signup_doctor.html')


@views.route('/signup-phar')
# When a pharmacist sign up into system
def signup_pharmacist():
    return render_template('signup_pharmacist.html')


@views.route('/doctor')
@login_required
# Doctor profile
def index_doctor():
    return render_template('doctor_profile.html')
