from App.database import db
from App.models import Author

class Publication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    author = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    coAuthor = db.relationship('Author', backref='publication', lazy=True)
    content = db.Column(db.String, nullable=False)
    citation = db.Column(db.String, nullable=False)

    def toJSON(self):
        return {
            'id': self.id,
            'name': self.name,
            'author': self.author,
            'coAuthor': self.coAuthor,
            'content': self.content,
            'citation': self.citation 
        }