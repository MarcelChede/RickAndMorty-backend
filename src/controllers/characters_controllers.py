from flask import jsonify
from src.services.characters_service import get_all_characters, get_character_by_id
from src.models.characters_model import character_schema

def get_characters(request):
    name = request.args.get('name', default="")
    page = int(request.args.get('page', default=1))
    per_page = int(request.args.get('per_page', default=20))
    characters = get_all_characters(name, page, per_page)
    return jsonify({
        'page': characters.page,
        'total_page': characters.pages,
        'items': character_schema.dump(characters.items)
    })

def get_character(request, id):
    character = get_character_by_id(id)
    if character:
        data = {'id': character.id, 'name': character.name, 'status': character.status, 'species': character.species,
                'type': character.type, 'gender': character.gender, 'origin_name': character.origin_name,
                'location_name': character.location_name, 'image': character.image}
        return jsonify(data)
    else:
        return jsonify({'message': 'Character not found'}), 404
