from flask import Blueprint, redirect, render_template, request, send_from_directory
from flask_jwt import jwt_required
from App.models import Author

from App.controllers import (
    get_author_email,
    get_all_pubs,
    get_all_authors,
    get_all_pubs_json,
    get_pub_by_name,
    search_pub,
    get_all_authors_json,
)

auth_views = Blueprint('auth_views', __name__, template_folder='../templates')

@auth_views.route('/login', methods=['GET', 'POST'])
def login_page():
    email = request.args.get('email')
    passw = request.args.get('pass')
    if email:
        author = get_author_email(email)
        author.check_password(author.password)
    return render_template('login.html')
