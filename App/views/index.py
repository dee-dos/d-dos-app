from flask import Blueprint, redirect, render_template, request, send_from_directory

from App.controllers import (
    get_all_pubs,
    get_all_authors,
    get_all_pubs_json,
    get_all_authors_json,
)

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    publications = get_all_pubs()
    authors = get_all_authors()
    return render_template('index.html', publications=publications, authors=authors)