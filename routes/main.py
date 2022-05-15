from flask import Blueprint, render_template, session, redirect, url_for, request, flash
from models.user import Users
from models.tags import Tags
from extensions import db

bp = Blueprint('main', __name__)


@bp.route('/')
def home_page():

    if "user" in session:
        return render_template("home.html")
    else:
        return redirect('/login')
        print('red to login')


@bp.route('/profile')
def profile_page():
    if "user" in session:
        found_user = Users.query.filter_by(name=session['user']).first()

        return render_template('profie.html', user=found_user, owner=True)
    else:
        return redirect('/login')

@bp.route('/<username>')
def show_user(username):
    if "user" in session:
        found_user = Users.query.filter_by(name=username).first()
        if found_user:
            if found_user.name == session['user']:
                return redirect(url_for('main.profile_page'))
            else:
                return render_template('profie.html', user=found_user, owner=False)
        else:
            flash('This user does not exist')
            return redirect(url_for('main.home_page'))

    else:
        return redirect(url_for('auth.login_page'))



@bp.route('/edit', methods=["POST","GET"])
def edit_page():
    if "user" in session:
        found_user = Users.query.filter_by(name=session['user']).first()

        if request.method == "POST":
            new_usrName = request.form["new_usrName"]
            new_usrBio = request.form["new_usrBio"]
            new_tag = request.form["new_tag"]

            if new_usrName != '':
                found_user.name = new_usrName
                session['user'] = new_usrName

                found_user.profbio = new_usrBio

                if new_tag != '':
                    tag = Tags()


                db.session.commit()
                flash("Your changes has been applied")
                return (redirect(url_for('main.profile_page')))

            else:
                flash("Fill all require inputs")



        return render_template('edit.html', user = found_user)

    else:
        return (redirect(url_for('auth.login_page')))

@bp.route('/test')
def test_page():
    found_user = Users.querry.filter_by(name=session['user']).first()
    return render_template('test.html', user=found_user)