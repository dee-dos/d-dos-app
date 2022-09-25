import flask_login
from flask_jwt import JWT
from App.models import Author


def authenticate(email, password):
    author = Author.query.filter_by(email=email).first()
    if author and author.check_password(password):
        return author
    return None

# Payload is a dictionary which is passed to the function by Flask JWT
def identity(payload):
    return Author.query.get(payload['identity'])

def login_user(author, remember):
    return flask_login.login_user(author, remember=remember)


def logout_author():
    flask_login.logout_author()

def setup_jwt(app):
    return JWT(app, authenticate, identity)