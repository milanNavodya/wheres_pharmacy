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


@views.route('/signup-usr')
# When a normal user try to sign up
def signup_user():
    return render_template('signup_user.html')


@views.route('/doctor')
@login_required
# Doctor profile
def index_doctor():
    return render_template('doctor_profile.html')


@views.route('/doctor/appointments')
@login_required
def doctor_appointments():
    return render_template('doctor_profile_appointments.html')


@views.route('/user')
@login_required
# Doctor profile
def index_user():
    return render_template('patient_menu.html')


@views.route('/user/setting')
@login_required
def settings_user_profile():
    return render_template('patient_profile_settings.html')


@views.route('/user/doctor')
@login_required
def doctor_for_user():
    return render_template('user_doctor_profile.html')


@views.route('/user/appointment', methods=['POST'])
@login_required
def place_appointment():
    return render_template('appointment_booking.html')


@views.route('/pharmacist')
@login_required
def index_pharmacist():
    return render_template('pharmacy_profile.html')


@views.route('/pharmacist/sales')
@login_required
def sale_order_details():
    return render_template('pharmacy_sales.html')


@views.route('/pharmacist/sales')
@login_required
def pharmacy_inventory():
    return render_template('pharmacy_inventory.html')
