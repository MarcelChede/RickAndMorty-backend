from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

class Character(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    status = db.Column(db.String(20))
    species = db.Column(db.String(50))
    type = db.Column(db.String(50))
    gender = db.Column(db.String(20))
    origin_name = db.Column(db.String(50))
    location_name = db.Column(db.String(50))
    image = db.Column(db.String(100))

class CharacterSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'status', 'species', 'type',
                  'gender', 'origin_name', 'location_name', 'image')

character_schema = CharacterSchema(many=True)