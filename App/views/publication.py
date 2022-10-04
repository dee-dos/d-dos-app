from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required


from App.controllers import (
    create_publication,
    get_pub,
    get_pub_by_name,
    update_pub,
    delete_publication,
    get_all_pubs,
    get_all_pubs_json,
)

pub_views = Blueprint('pub_views', __name__, template_folder='../templates')

# Jinja Routes

@pub_views.route('/publications', methods=['GET'])
def get_pub_page():
    publications = get_all_pubs()
    return render_template('publications.html', publications=publications)

@pub_views.route('/publication/<id>')
def pub_info(id):
    publication = get_pub(id)
    return render_template('pub-info.html', publication=publication)

# JS Routes

@pub_views.route('/static/authors')
def static_user_page():
  return send_from_directory('static', 'static-user.html')

# API Routes

@pub_views.route('/api/publications', methods=['GET'])
def get_all_pubs_action():
    publications = get_all_pubs_json()
    return jsonify(publications)

@pub_views.route('/api/publications/id', methods=['GET'])
def get_pub_action():
    data = request.json
    pub = get_pub(data['id'])
    if pub:
        return pub.toJSON()
    return jsonify({"message":"Publication not found!"})

@pub_views.route('/api/publications', methods=['POST'])
def create_pub_action():
    data = request.json
    pub = create_pub_action(data['name'], data['author'], data['content'], data['citation'])
    return jsonify({"message":"Publication created successfully!"})

@pub_views.route('/api/publications', methods=['PUT'])
def update_pub_action():
    data = request.json
    pub = get_pub(data['id'])
    if pub:
        update_pub(data['id'], data['name'], data['author'], data['content'], data['citation'])
        return jsonify({"message":"Publication updated successfully!"})
    return jsonify({"message":"Publication not found!"})

@pub_views.route('/api/publications', methods=['DELETE'])
def delete_pub_action():
    data = request.json
    pub = get_pub(data['id'])
    if pub:
        delete_publication(data['id'])
        return jsonify({"message":"Publication deleted successfully!"})
    return jsonify({"message":"Publication not found!"})