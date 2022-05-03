from flask import Flask, session
from .extensions import db
from .routes import main, auth

from datetime import timedelta


def create_app():
    app = Flask(__name__)
    app.secret_key = "qazxdr4321"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.permanent_session_lifetime = timedelta(minutes=5)

    db.init_app(app)

    app.register_blueprint(main.bp)
    app.register_blueprint(auth.bp)



    return app



# db.create_all(app=create_app())