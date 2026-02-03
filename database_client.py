import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Carga las variables del archivo .env
load_dotenv()

def get_db_connection():
    uri = os.getenv("MONGO_URI")
    client = MongoClient(uri)
    # Esto conecta a la base de datos que creaste en la Parte A
    db = client['curso_admin_datos']
    return db['pokedex_data']

if __name__ == "__main__":
    # Prueba de conexión rápida
    collection = get_db_connection()
    print(f"Conexión exitosa a la colección: {collection.name}")