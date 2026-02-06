# load_pokemon_to_mongo.py
import os
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv

# ==============================
# 1. Cargar variables de entorno
# ==============================
load_dotenv()

uri = os.getenv("MONGO_URI")
if not uri:
    raise ValueError("No se encontró MONGO_URI en el archivo .env")

# ==============================
# 2. Conexión a MongoDB
# ==============================
client = MongoClient(uri)

db = client["curso_admin_datos"]
collection = db["dataset_grupo"]

print("Conectado a MongoDB")

# ==============================
# 3. Leer el CSV
# ==============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "pokemon_dataset.csv")

if not os.path.exists(csv_path):
    raise FileNotFoundError(f"No se encontró el archivo: {csv_path}")

df = pd.read_csv(csv_path)
print(f"Dataset cargado con {len(df)} registros")


# ==============================
# 4. Insertar en MongoDB
# ==============================
print("Limpiando colección antes de insertar...")
collection.delete_many({})

data = df.to_dict(orient="records")

if data:
    result = collection.insert_many(data)
    print(f"{len(result.inserted_ids)} documentos insertados correctamente")
else:
    print("El dataset está vacío, no se insertó nada")

