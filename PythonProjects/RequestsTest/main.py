import requests

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "aec6f1e6c4e62c8ae51fdc8aec219dd6"
HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN
}

body_sozdania = {
    "name": "generate",
    "photo_id": 35
}

responce = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_sozdania)
print(responce.text)


pokemon_id = responce.json()['id']


body_update = {
    "pokemon_id": pokemon_id,
    "name": "Забавник",
    "photo_id": 23
}

responce_update = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_update)
print(responce_update.text) 

body_add_pokeball = {
    "pokemon_id": pokemon_id
}

responce_add = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(responce_add.text)




