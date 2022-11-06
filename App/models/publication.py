from App.database import db
from .author import *
from .model import *

class Publication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    author = db.Column(db.ForeignKey('author.id'))
    coauthors = db.relationship('Author', secondary=pub_tree)
    content = db.Column(db.String, nullable=False)
    citation = db.Column(db.String, nullable=False)

    def toJSON(self):

        print(type(self.author))

        return {
            'id': self.id,
            'name': self.name,
            'author': self.author,
            'content': self.content,
            'citation': self.citation,
        }