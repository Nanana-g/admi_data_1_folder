import requests
import pandas as pd
from time import sleep

def fetch_pokemon_data(limit=600):
    print(f"Obteniendo datos de {limit} Pokémon...")
    pokemon_list = []

    for i in range(1, limit + 1):
        url = f"https://pokeapi.co/api/v2/pokemon/{i}"
        try:
            response = requests.get(url, timeout=10)  # timeout de 10 segundos
            response.raise_for_status()               # lanza error si no es 200
            data = response.json()

            pokemon_list.append({
                "id": data["id"],
                "name": data["name"],
                "height": data["height"],
                "weight": data["weight"],
                "base_experience": data["base_experience"],
                "type": data["types"][0]["type"]["name"]
            })
            print(f"OK -> {i}: {data['name']}")
            
            # pequeña pausa para no saturar la API
            sleep(0.2)

        except requests.exceptions.Timeout:
            print(f"Timeout con el Pokémon {i} (URL: {url}) – lo salto.")
            continue
        except requests.exceptions.RequestException as e:
            print(f"Error con el Pokémon {i}: {e}")
            continue

    df = pd.DataFrame(pokemon_list)
    df.to_csv("pokemon_dataset.csv", index=False, encoding="utf-8")
    print("¡Archivo pokemon_dataset.csv generado con éxito!")

if __name__ == "__main__":
    fetch_pokemon_data()