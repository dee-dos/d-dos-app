from App.database import db
from .author import *
from .publication import *

pub_tree = db.Table('pub_tree',
    db.Column('publication', db.Integer, db.ForeignKey('publication.id')),
    db.Column('coauthors', db.Integer, db.ForeignKey('author.id'))
)