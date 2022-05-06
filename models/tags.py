from extensions import db


class Tags(db.Model):
    category = db.Column("category", db.String(100), nullable=False)
    content = db.Column("content", db.String(10000))


    def __init__(self, category):
        self.category = category


