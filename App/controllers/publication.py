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

    pubs = [pub.toJSON() for pub in pubs]
    return pubs

def delete_publication(id):
    pub = get_pub(id)
    if pub:
        db.session.delete(pub)
        db.session.commit()
    return None

def update_pub(id, name, content, citation):
    pub = get_pub(id)
    if pub:
        pub.name = name
        pub.content = content
        pub.citation = citation
        db.session.add(pub)
        return db.session.commit()
    return None
    