from flask import Flask
from flask_cors import CORS
from src.models.characters_model import db
from src.routes.characters_routes import character_routes
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
db.init_app(app)
CORS(app)

app.register_blueprint(character_routes)

if __name__ == '__main__':
    app.run(debug=True)