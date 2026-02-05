from pymongo import MongoClient

# ==============================
# 1. CADENA DE CONEXIÓN (URI)
# ==============================
# Reemplaza USUARIO, CONTRASEÑA y CLUSTER por los datos de MongoDB Atlas
uri = "mongodb+srv://USUARIO:CONTRASEÑA@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority"

# ==============================
# 2. CONEXIÓN AL CLUSTER
# ==============================
client = MongoClient(uri)

# ==============================
# 3. BASE DE DATOS Y COLECCIÓN
# ==============================
db = client["curso_admin_datos"]
collection = db["dataset_grupo"]

# ==============================
# 4. CONSULTA 1: Conteo total
# ==============================
total_docs = collection.count_documents({})
print(f"Total de documentos en la colección: {total_docs}")

# ==============================
# 5. CONSULTA 2: Mostrar 5 documentos
# ==============================
print("\n--- 5 documentos ---")
for doc in collection.find().limit(5):
    print(doc)

# ==============================
# 6. CONSULTA 3: Consulta con filtro
# (ajustar el campo según el dataset)
# ==============================
print("\n--- Consulta con filtro ---")
for doc in collection.find({"country": "USA"}).limit(5):
    print(doc)

# ==============================
# 7. CONSULTA 4: Ordenamiento y límite
# (ajustar el campo según el dataset)
# ==============================
print("\n--- Ordenamiento y límite ---")
for doc in collection.find().sort("price", -1).limit(5):
    print(doc)
