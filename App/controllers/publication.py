from App.models import Publication
from App.models import Author
from App.database import db

def create_publication(name, author, content, citation):
    newPub = Publication(name=name, author=author, content=content, citation=citation)
    db.session.add(newPub)
    db.session.commit()
    return newPub

def get_pub_by_name(name):
    return Publication.query.filter_by(fname=fname).first()

def get_pub(id):
    return Publication.query.get(id)

def get_all_pubs():
    return Publication.query.all()

def get_all_pubs_json():
    pubs = Publication.query.all()
    if not pubs:
        return []
    pubs = [publication.toJSON() for publication in publications]
    return pubs

def update_author(id, fname, lname):
    author = get_author(id)
    if author:
        author.fname = fname
        author.lname = lname
        db.session.add(author)
        return db.session.commit()
    return None
    