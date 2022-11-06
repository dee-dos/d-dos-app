from App.models import Publication
from App.models import Author
from App.database import db
from .author import *

def create_publication(name, author, content, citation):
    newPub = Publication(name=name, author=author, content=content, citation=citation)
    db.session.add(newPub)
    db.session.commit()
    return newPub

def search_pub(search):
    return Publication.query.filter(
        Publication.name.like( '%'+search+'%' )
    )

def get_pub_by_name(name):
    return Publication.query.filter_by(name=name).first()

def get_pub_by_author(id):
    pubs = Publication.query.filter_by(author=id).all()

    if not pubs:
        return []

    pubs = [pub.toJSON() for pub in pubs]
    return pubs

def get_pub(id):
    return Publication.query.get(id)

def get_all_pubs():
    return Publication.query.all()

def get_all_pubs_json():
    pubs = Publication.query.all()
    if not pubs:
        return []

    pubs = [pub.toJSON() for pub in pubs]
    return pubs

def delete_publication(id):
    pub = get_pub(id)
    if pub:
        db.session.delete(pub)
        db.session.commit()
    return None

def update_pub(id, name, author, content, citation):
    pub = get_pub(id)
    if pub:
        pub.name = name
        pub.content = content
        pub.citation = citation
        db.session.add(pub)
        return db.session.commit()
    return None

def add_pub_co_author(id, co_author):
    pub = get_pub(id)
    if pub:
        author = get_author(co_author)
        pub.coauthors.append(author)
        db.session.add(pub)
        return db.session.commit()
    return None




    

    