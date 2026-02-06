# 📦 Trabajo Práctico – Administración de Datos

**Pipeline de datos con Python y MongoDB Atlas**

---

## 📌 Descripción

Este proyecto implementa un flujo completo de manejo de datos utilizando Python y MongoDB Atlas. El trabajo se estructura en tres etapas:

* **Parte A – Extracción:** obtención de datos desde una API pública.
* **Parte B – Carga:** almacenamiento del dataset en una base de datos NoSQL (MongoDB Atlas).
* **Parte C – Consultas:** realización de consultas sobre los datos almacenados.

El dataset utilizado corresponde a información de Pokémon obtenida desde la **PokeAPI**.

---

## 🧰 Tecnologías utilizadas

* Python 3
* MongoDB Atlas
* PyMongo
* Pandas
* Requests
* python-dotenv

---

## 📂 Estructura del proyecto

```
├── .gitignore
├── extract_pokemon.py          # Parte A: extracción de datos desde la API
├── load_pokemon_to_mongo.py    # Parte B: carga del dataset en MongoDB Atlas
├── conexion_mongodb            # Parte Conexión a Python y consultas
├── verificación.py             # Script de verificación de datos del MongoDB Atlas
├── requirements.txt            # Requisitos para instalar
└── README.md                   # Documentación del proyecto
```

---

## ⚙️ Configuración del entorno

### 1️⃣ Instalación de dependencias y creación/activación del ambiente virtual

Crear venv:
```bash
python -m venv venv
```
---

Activar venv en windows:
```bash
venv/scripts/activate
```

Instalar dependencias
```bash
pip install -r requirements.txt
```

---

## 🔐 Variables de entorno

Se debe crear un archivo `.env` en la raíz del proyecto con la siguiente variable:

```env
MONGO_URI=mongodb+srv://nanana:7fd5DRWTK0r14oNW@cluster0.ian5vxv.mongodb.net/
```

> ⚠️ El archivo `.env` no debe subirse al repositorio por razones de seguridad.

---

## ▶️ Ejecución del proyecto

### 🔹 Parte A – Extracción de datos

Obtiene información desde la PokeAPI y genera un archivo CSV con los datos.

```bash
python extract_pokemon.py
```

Resultado esperado:

* Archivo `pokemon_dataset.csv` con aproximadamente 600 registros.

---

### 🔹 Parte B – Carga de datos en MongoDB Atlas

Carga el dataset en MongoDB Atlas utilizando PyMongo. Antes de la inserción, la colección se limpia para evitar duplicados.

```bash
python load_pokemon_to_mongo.py
```

Resultado esperado:

* Creación automática de la base de datos y la colección.
* Inserción exitosa de los documentos.

---

### 🔹 Verificación

Permite comprobar la existencia de bases de datos, colecciones y la cantidad de documentos cargados.

```bash
python verificar_mongo.py
```

---

### 🔹 Parte C – Consultas

Se realizan consultas sobre la colección creada, incluyendo:

* Conteo total de documentos.
* Visualización de registros.
* Filtros por tipo de Pokémon.
* Ordenamiento por experiencia base.

---

## 📊 Estructura del dataset

Cada documento almacenado en MongoDB contiene los siguientes campos:

* `id` (int)
* `name` (string)
* `height` (int)
* `weight` (int)
* `base_experience` (int)
* `type` (string)

---

## 🧠 Consideraciones finales

* MongoDB crea automáticamente la base de datos y la colección al insertar datos.
* El proceso de carga evita la duplicación de registros.
* El proyecto es reproducible y permite validar fácilmente cada etapa del proceso.

---

## 👥 Distribución del trabajo

* **Parte A:** Extracción de datos desde la API.
* **Parte B:** Carga del dataset en MongoDB Atlas.
* **Parte C:** Consultas sobre los datos almacenados.

---

📌 **Trabajo Práctico – Administración de Datos**
