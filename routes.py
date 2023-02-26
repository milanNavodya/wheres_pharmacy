from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from flask_login import login_user, logout_user, login_required
from config import db


route_obj = Blueprint('routes', __name__)  # create a Blueprint object that we name 'auth'

