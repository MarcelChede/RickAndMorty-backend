from flask import Blueprint, request
from src.controllers.characters_controllers import get_characters, get_character

character_routes = Blueprint('character_routes', __name__)

@character_routes.route('/search', methods=['GET'])
def search_characters():
    return get_characters(request)

@character_routes.route('/search/<int:id>', methods=['GET'])
def search_character_by_id(id):
    return get_character(request, id)
