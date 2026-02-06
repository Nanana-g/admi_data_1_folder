# verificar_mongo.py
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv("MONGO_URI")
client = MongoClient(uri)

print("Bases de datos:")
print(client.list_database_names())

db = client["curso_admin_datos"]
print("\nColecciones:")
print(db.list_collection_names())

collection = db["dataset_grupo"]
print("\nCantidad de documentos:")
print(collection.count_documents({}))
