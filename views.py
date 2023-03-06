from flask import Blueprint, render_template, request, flash, jsonify, session, redirect, url_for
from flask_login import login_required
from config import db
from datetime import datetime
import routes
from models import User

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


# Routes for doctors
@views.route('/doctor')
@login_required
# Doctor profile
def index_doctor():
    return render_template('doctor_profile.html')


@views.route('/doctor/appointments')
@login_required
def doctor_appointments():
    return render_template('doctor_profile_appointments.html')


# Routes for Patients
@views.route('/user')
@login_required
# Doctor profile
def index_user():
    return render_template('patient_menu.html')


@views.route('/user/setting')
@login_required
def settings_user_profile():
    user_id = session.get('id')
    user = User.query.filter_by(id=user_id).first()
    if user.user_role == 'patient':
        return render_template('patient_profile_settings.html')
    else:
        return redirect(url_for('views.page_not_found'))


@views.route('/user/doctor')
@login_required
def doctor_for_user():
    user_id = session.get('id')
    user = User.query.filter_by(id=user_id).first()
    if user.user_role == 'patient':
        return render_template('user_doctor_profile.html')
    else:
        return redirect(url_for('views.page_not_found'))


@views.route('/user/buy-med')
@login_required
def buy_medicine():
    user_id = session.get('id')
    user = User.query.filter_by(id=user_id).first()
    if user.user_role == 'patient':
        return render_template('patient_buy_medicine.html')
    else:
        return redirect(url_for('views.page_not_found'))


@views.route('/user/appointment', methods=['POST'])
@login_required
def place_appointment():
    user_id = session.get('id')
    user = User.query.filter_by(id=user_id).first()
    if user.user_role == 'patient':
        return render_template('appointment_booking.html')
    else:
        return redirect(url_for('views.page_not_found'))


# Routes for Pharmacists
@views.route('/pharmacist')
@login_required
def index_pharmacist():
    user_id = session.get('id')
    user = User.query.filter_by(id=user_id).first()
    if user.user_role == 'pharmacist':
        return render_template('pharmacy_profile.html')
    else:
        return redirect(url_for('views.page_not_found'))


@views.route('/pharmacist/sales')
@login_required
def sale_order_details():
    user_id = session.get('id')
    user = User.query.filter_by(id=user_id).first()
    if user.user_role == 'pharmacist':
        return render_template('pharmacy_sales.html')
    else:
        return redirect(url_for('views.page_not_found'))


@views.route('/pharmacist/inventory')
@login_required
def pharmacy_inventory():
    return render_template('pharmacy_inventory.html')


@views.route('/page-not-found')
def page_not_found():
    return render_template('404-error.html')
