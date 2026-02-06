from pymongo import MongoClient
import os
from dotenv import load_dotenv

# ==============================
# 1. Cargar variables de entorno
# ==============================
load_dotenv()
uri = os.getenv("MONGO_URI")

client = MongoClient(uri)

# ==============================
# 2. Base de datos y colección
# ==============================
db = client["curso_admin_datos"]
collection = db["dataset_grupo"]

# ==============================
# 3. Consulta 1: Conteo total
# ==============================
total_docs = collection.count_documents({})
print(f"Total de documentos en la colección: {total_docs}")

# ==============================
# 4. Consulta 2: Mostrar 5 documentos
# ==============================
print("\n--- 5 documentos ---")
for doc in collection.find().limit(5):
    print(doc)

# ==============================
# 5. Consulta 3: Filtro por tipo
# ==============================
print("\n--- Pokémon de tipo 'fire' ---")
for doc in collection.find({"type": "fire"}).limit(5):
    print(doc)

# ==============================
# 6. Consulta 4: Ordenamiento
# ==============================
print("\n--- Pokémon con mayor base_experience ---")
for doc in collection.find().sort("base_experience", -1).limit(5):
    print(doc)

