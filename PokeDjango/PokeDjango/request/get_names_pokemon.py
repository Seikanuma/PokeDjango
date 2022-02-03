import os
import requests


response = requests.get("https://pokeapi.co/api/v2/pokemon")

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

def get_names_pokemons():

    all_pokes = response.json()

    return all_pokes