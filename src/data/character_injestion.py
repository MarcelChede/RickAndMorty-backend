import psycopg2
import json
from dotenv import load_dotenv
import os

load_dotenv()

json_file = 'src/data/allChars.json'

with open(json_file, 'r', encoding='utf-8') as file:
    json_data = json.load(file)

db_connection = {
    'dbname': os.getenv('DATABASE'),
    'user': os.getenv('USER'),
    'password': os.getenv('PASSWORD'),
    'host': os.getenv('HOST'),
    'port': os.getenv('PORT')
}


def populates():
    try:
        with psycopg2.connect(**db_connection) as connection:
            with connection.cursor() as cursor:
                cursor.execute('''
                    CREATE TABLE characters (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(50),
                        status VARCHAR(20),
                        species VARCHAR(50),
                        type VARCHAR(50),
                        gender VARCHAR(20),
                        origin_name VARCHAR(50),
                        location_name VARCHAR(50),
                        image VARCHAR(100)
                    )
                ''')

                for data in json_data:
                    cursor.execute('''
                        INSERT INTO characters (
                            name, status, species, type, gender,
                            origin_name, location_name, image
                        )
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    ''', (
                        data['name'], data['status'], data['species'], data['type'], data['gender'],
                        data['origin']['name'], data['location']['name'], data['image']
                    ))

            connection.commit()

        print("Database successfully created and populated!")
    except psycopg2.Error as e:
        print("Error:", e)


populates()
