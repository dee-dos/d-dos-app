from App.database import db
from App.models import author

class Publication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    author = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    author1 = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=True)
    author2 = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=True)
    author3 = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=True)
    author4 = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=True)
    author5 = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=True)
    content = db.Column(db.String, nullable=False)
    citation = db.Column(db.String, nullable=False)

    def toJSON(self):
        return {
            'id': self.id,
            'name': self.name,
            'author': self.author,
            'author1': self.author1,
            'author2': self.author2,
            'author3': self.author3,
            'author4': self.author4,
            'author5': self.author5,
            'content': self.content,
            'citation': self.citation
        }