from extensions import db
from datetime import datetime

class Messages(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    grantor = db.Column("grantor", db.String(20), nullable=False)
    content = db.Column("content", db.String(100), nullable=False)
    vision = db.Column("vision", db.Boolean(), nullable=False)
    date = db.Column("date", db.String(20))



    def __init__(self, grantor, content):
        self.grantor = grantor
        self.content = content
        self.date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.vision = True

    def __repr__(self):
        return f'<Message: {self.grantor} : {self.content} - {str(self.date)} : {self.vision}>'

