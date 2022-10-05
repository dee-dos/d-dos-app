from App.database import db
from .author import *

class Publication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    author = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    coauthors = db.relationship('Author', backref='Publication', overlaps="Publication,coauthors", lazy='select')
    content = db.Column(db.String, nullable=False)
    citation = db.Column(db.String, nullable=False)

    def toJSON(self):
        return {
            'id': self.id,
            'name': self.name,
            'author': self.author.toJSON,
            'coauthors': self.coauthors.toJSON,
            'content': self.content,
            'citation': self.citation
        }