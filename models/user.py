from extensions import db
from datetime import datetime

class Users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100), nullable=False)
    password = db.Column("password", db.String(100), nullable=False)



    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __repr__(self):
        return f'<User {self.name}>'



