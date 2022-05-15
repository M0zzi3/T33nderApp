from extensions import db

class Users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(20), nullable=False)
    password = db.Column("password", db.String(100), nullable=False)
    profpic = db.Column("profpic", db.String(100))
    proftags = db.Column("proftags", db.String(1000))
    profbio = db.Column("profbio", db.String(500))
    friends = db.Column("friends", db.String(2000))



    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.profpic = 'default_profpic'
        self.proftags = ' '
        self.profbio = f'Hello my name is {self.name}! Whats up?'
        self.friends = 'nobody'

    def __repr__(self):
        return f'<User: {self.name}>'



