from src.models.characters_model import Character


def get_all_characters(name="", page=1, per_page=20):
    characters = Character.query.filter(Character.name.ilike(f"%{name}%")).order_by(
        Character.id.asc()).paginate(page=page, per_page=per_page)
    return characters


def get_character_by_id(id):
    return Character.query.get(id)


def get_characters_by_gender(name, page=1, per_page=20):
    characters = Character.query.filter(Character.name.ilike(f"%{name}%")).order_by(
        Character.id.asc()).paginate(page=page, per_page=per_page)
    return characters
