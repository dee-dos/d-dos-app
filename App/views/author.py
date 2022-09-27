from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required


from App.controllers import (
    create_author,
    get_author,
    get_all_authors,
    get_all_authors_json,
)

author_views = Blueprint('author_views', __name__, template_folder='../templates')


@author_views.route('/authors', methods=['GET'])
def get_author_page():
    authors = get_all_authors()
    return render_template('authors.html', authors=authors)

@author_views.route('/api/authors')
def client_app():
    authors = get_all_authors_json()
    return jsonify(authors)

@author_views.route('/author/<id>', methods=['GET'])
def author_profile(id):
    author = get_author(id)
    return render_template('profile.html', author=author)

''' @author_views.route('/static/authors')
def static_user_page():
  return send_from_directory('static', 'static-user.html') '''