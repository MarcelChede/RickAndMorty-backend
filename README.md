Rick and Morty API - Flask Backend

This project is a Flask backend to provide a RESTful API for accessing information about characters from the Rick and Morty universe.

Project Structure

    - app.py: Main file of the Flask application
    - src/
    - models/: Data model definitions and database configuration
    - services/: Business logic and interactions with the database
    - controllers/: Controllers to handle HTTP requests
    - routes/: API route definitions


Requirements

    pip install -r requirements.txt 

Database Configuration

    The application uses PostgreSQL as the database. Make sure you have PostgreSQL installed locally. You can configure the database connection in the app.py file.

Endpoints

    GET /search
    GET /search/int:id
    GET /search/name/string:name
