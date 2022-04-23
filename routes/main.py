from flask import Blueprint, render_template, session, redirect, url_for

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
    return render_template('profie.html')
