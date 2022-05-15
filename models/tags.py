from extensions import db

class Tags(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    content = db.Column("name", db.String(20))
    category = db.Column("category", db.String(20))

    def __init__(self, content, category):
        self.content = content
        self.category = category


    def __repr__(self):
        return f'<Tag: {self.content} - {self.category}>'


