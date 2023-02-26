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
