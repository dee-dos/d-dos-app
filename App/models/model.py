from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

pub_tree = db.Table('pub_tree',
    db.Column('author', db.Integer, db.ForeignKey('author.id')),
    db.Column('publication', db.Integer, db.ForeignKey('publication.id'))
)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String, nullable=False)
    lname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    publications = db.relationship('Publication', backref='authors', lazy='select', secondary=pub_tree)

    def __init__(self, fname, lname, email, password):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.set_password(password)

    def toJSON(self):
        return{
            'id': self.id,
            'fname': self.fname,
            'lname': self.lname,
            'email': self.email
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

class Publication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    author = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    content = db.Column(db.String, nullable=False)
    citation = db.Column(db.String, nullable=False)

    def toJSON(self):
        return {
            'id': self.id,
            'name': self.name,
            'author': self.author.toJSON(),
            'co-authors': self.authors,
            'content': self.content,
            'citation': self.citation
        }