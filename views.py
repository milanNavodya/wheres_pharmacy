from flask import Blueprint, render_template, request, flash, jsonify, session, redirect, url_for
from flask_login import login_required
from config import db
from datetime import datetime, date
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


@views.route('/admin')
@login_required
def index_admin():
    user_id = session.get('id')
    user = User.query.filter_by(id=user_id).first()
    if user.user_role == 'admin':
        return render_template('admin.html')
    else:
        return redirect(url_for('views.page_not_found'))


@views.route('/admin/add-doctor', methods=['GET', 'POST'])
@login_required
def admin_add_doctor():
    user_id = session.get('id')
    user = User.query.filter_by(id=user_id).first()
    if user.user_role == 'admin':
        if request.method == 'GET':
            return render_template('admin.html')
        else:
            secret_key = request.form.get('secretkey')
            name = request.form.get('name')
            role = 'doctor'
            doctor = User.query.filter_by(secret_key=secret_key).first()
            if doctor:
                flash("Secret key already in used!")
                return redirect(url_for('views.index_admin'))
            else:
                new_doctor = User(full_name=name, email=None, password=None, gender=None, dob=None, address=None,
                                  mobile=None, position=None, category=None,
                                  pharmacy_reg_no=None, user_role=role, secret_key=secret_key)
                db.session.add(new_doctor)
                db.session.commit()
                return redirect(url_for('views.index_admin'))
    else:
        return redirect(url_for('views.page_not_found'))


# Routes for doctors
@views.route('/doctor')
@login_required
# Doctor profile
def index_doctor():
    user_id = session.get('id')
    user = User.query.filter_by(id=user_id).first()
    if user.user_role == 'doctor':
        return render_template('doctor_profile.html', name=user.full_name, category=user.category)
    else:
        return redirect(url_for('views.page_not_found'))


@views.route('/doctor/appointments')
@login_required
def doctor_appointments():
    user_id = session.get('id')
    user = User.query.filter_by(id=user_id).first()
    if user.user_role == 'doctor':
        return render_template('doctor_profile_appointments.html', name=user.full_name, category=user.category)
    else:
        return redirect(url_for('views.page_not_found'))


# Routes for Patients
@views.route('/user')
@login_required
# Doctor profile
def index_user():
    user_id = session.get('id')
    user = User.query.filter_by(id=user_id).first()
    if user.user_role == 'patient':
        return render_template('patient_menu.html', name=user.full_name)
    else:
        return redirect(url_for('views.page_not_found'))


@views.route('/user/user_details')
@login_required
def user_profile_details():
    user_id = session.get('id')
    user = User.query.filter_by(id=user_id).first()
    age = date.today().year - user.dob.year
    if user.user_role == 'patient':
        return render_template('patient_profile_settings.html', name=user.full_name, age=age, gender=user.gender)
    else:
        return redirect(url_for('views.page_not_found'))


@views.route('/user/chat')
@login_required
def chat():
    user_id = session.get('id')
    user = User.query.filter_by(id=user_id).first()
    if user.user_role == 'patient':
        return render_template('chatUi.html')
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


@views.route('/user/buy-med', methods=['GET', 'POST'])
@login_required
def buy_medicine():
    user_id = session.get('id')
    user = User.query.filter_by(id=user_id).first()
    if user.user_role == 'patient':
        if request.method == 'GET':
            return render_template('patient_buy_medicine.html', name=user.full_name)
        else:
            # TODO: place an order, store in table
            pass
    else:
        return redirect(url_for('views.page_not_found'))


@views.route('/user/appointment')
@login_required
def place_appointment():
    user_id = session.get('id')
    user = User.query.filter_by(id=user_id).first()
    if user.user_role == 'patient':
        return render_template('appointment_booking.html', name=user.full_name, phone=user.mobile)
    else:
        return redirect(url_for('views.page_not_found'))


@views.route('/user/location')
@login_required
def get_location():
    user_id = session.get('id')
    user = User.query.filter_by(id=user_id).first()
    if user.user_role == 'patient':
        """Get longitude and latitude of user"""
        import location as loc
        loc.inputs()
        loc.makeMap()
        loc.add_CSV_values_to_map()
        loc.add_user()
        loc.draw_circle_around_user()
        return render_template('map.html')
    else:
        return redirect(url_for('views.page_not_found'))


# Routes for Pharmacists
@views.route('/pharmacist')
@login_required
def index_pharmacist():
    user_id = session.get('id')
    user = User.query.filter_by(id=user_id).first()
    if user.user_role == 'pharmacist':
        return render_template('pharmacy_profile.html', name=user.full_name)
    else:
        return redirect(url_for('views.page_not_found'))


@views.route('/pharmacist/sales')
@login_required
def sale_order_details():
    user_id = session.get('id')
    user = User.query.filter_by(id=user_id).first()
    if user.user_role == 'pharmacist':
        return render_template('pharmacy_sales.html', name=user.full_name)
    else:
        return redirect(url_for('views.page_not_found'))


@views.route('/pharmacist/inventory')
@login_required
def pharmacy_inventory():
    user_id = session.get('id')
    user = User.query.filter_by(id=user_id).first()
    if user.user_role == 'pharmacist':
        return render_template('pharmacy_inventory.html', name=user.full_name)
    else:
        return redirect(url_for('views.page_not_found'))


@views.route('/pharmacist/inventory/create', methods=['POST', 'GET'])
@login_required
def inventory_create():
    # todo : add inventory create form
    if request.method == 'GET':
        return "create form"
    else:
        """update database"""
        return 'create form'


@views.route('/pharmacist/inventory/update', methods=['POST'])
@login_required
def inventory_update():
    # todo : add inventory update form
    return 'update form'


@views.route('/pharmacist/inventory/delete', methods=['POST'])
@login_required
def inventory_delete():
    # todo : add inventory delete form
    return 'deleted'


@views.route('/page-not-found')
def page_not_found():
    return render_template('404-error.html')
