from flask import Blueprint, render_template, session, redirect, url_for
from models.user import Users
from extensions import db

bp = Blueprint('main', __name__)


@bp.route('/')
def home_page():

    if "user" in session:
        return render_template("home.html")
    else:
        return redirect('/login')


@bp.route('/profile')
def profile_page():
    if "user" in session:
        found_user = Users.query.filter_by(name=session['user']).first()

        return render_template('profie.html', user=found_user)
    else:
        return redirect('/login')
