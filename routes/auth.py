from flask import Blueprint, render_template, session, redirect,  url_for, request, flash
from models.user import Users
from extensions import db



bp = Blueprint('auth', __name__)

@bp.route('/login', methods=["POST","GET"])
def login_page():

    if request.method == "POST":
        logg_ursName = request.form["logg_usrName"]
        logg_ursPassword = request.form["logg_usrPassword"]

        found_user = Users.query.filter_by(name=logg_ursName).first()

        if found_user and found_user.password == logg_ursPassword:

            session['user'] = logg_ursName
            session.permanent = True

            return redirect(url_for('main.profile_page'))

        else:
            flash('Wrong user or password')


    return render_template('login.html')


@bp.route('/register', methods=["POST","GET"])
def register_page():
    if request.method == "POST":
        session.permanent = True
        new_usrName = request.form["new_usrName"]
        new_usrPassword = request.form["new_usrPassword"]

        print(new_usrName, new_usrPassword)

        found_user = Users.query.filter_by(name=new_usrName).first()


        if found_user != None:
            flash("This user name is ocupaited")

        else:
            usr = Users(new_usrName, new_usrPassword)
            db.session.add(usr)
            db.session.commit()

            session['user'] = new_usrName

            return redirect(url_for('main.profile_page'))


    return render_template('register.html')



@bp.route('/logout')
def logout():

    try:
        last_user = session['user']
        flash(f"You have been logged out {last_user}")
        session.pop('user')
    except KeyError:
        flash(f"You haven't been logged")
    return redirect(url_for('auth.login_page'))
