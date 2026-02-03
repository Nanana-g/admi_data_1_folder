import requests
import pandas as pd

def fetch_pokemon_data(limit=600): # El requisito pide al menos 500 filas
    print(f"Obteniendo datos de {limit} Pokémon...")
    pokemon_list = []
    
    for i in range(1, limit + 1):
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{i}")
        if response.status_code == 200:
            data = response.json()
            # Extraemos solo lo que nos interesa para el dataset
            pokemon_list.append({
                "id": data["id"],
                "name": data["name"],
                "height": data["height"],
                "weight": data["weight"],
                "base_experience": data["base_experience"],
                "type": data["types"][0]["type"]["name"]
            })
    
    df = pd.DataFrame(pokemon_list)
    df.to_csv("pokemon_dataset.csv", index=False)
    print("¡Archivo pokemon_dataset.csv generado con éxito!")

if __name__ == "__main__":
    fetch_pokemon_data()