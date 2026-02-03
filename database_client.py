import os
from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv()

def get_db_connection():
    uri = os.getenv("MONGO_URI")
    client = MongoClient(uri)
    db= client['admin_datos']
    return db['pokedex_data']

if __name__ == "__main__":
    collection= get_db_connection()
    print(f"Conexión exitosa a la colección: {collection.name}")