from App.models import Author
from App.database import db

def create_author(fname, lname, email, password):
    newAuthor = Author(fname=fname, lname=lname, email=email, password=password)
    db.session.add(newAuthor)
    db.session.commit()
    return newAuthor

def get_author_by_fname(fname):
    return Author.query.filter_by(fname=fname).first()

def get_author_by_lname(lname):
    return Author.query.filter_by(lname=lname).first()

def get_author_email(email):
    return Author.query.filter_by(email=email).first()

def get_author(id):
    return Author.query.get(id)

def get_all_authors():
    return Author.query.all()

def get_all_authors_json():
    authors = Author.query.all()
    if not authors:
        return []
    authors = [author.toJSON() for author in authors]
    return authors

def delete_author(id):
    author = get_author(id)
    if author:
        db.session.delete(author)
        db.session.commit()
    return None

def update_author(id, fname, lname, email, password):
    author = get_author(id)
    if author:
        author.fname = fname
        author.lname = lname
        author.email = email
        author.password = password
        db.session.add(author)
        return db.session.commit()
    return None

def get_author_pubs(id):
    author = get_author(id)
    pubs = author.publications
    return pubs