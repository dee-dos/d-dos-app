from App.models import Publication
from App.models import Author
from App.database import db
from anytree import Node, PreOrderIter
from collections import UserList

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

def build_pub_tree(id):
    pub = get_pub(id)

    pa = Node(pub.author)
    authors = pub.coauthors

    for author in authors:
        author.id = Node(author.id, parent=pa)
        build_pub_tree(author.id)

class PubList(UserList):

    def remove(self, s = None):
        raise RuntimeError("Deletion not allowed")

    def pop(self, s = None):
        raise RuntimeError("Deletion not allowed")

def print_pub_tree(id):
    pubtree = build_pub_tree(id)
    Pubs = PubList()

    for node in PreOrderIter(pubtree):
        Pubs = node.Author.publications 




    

    