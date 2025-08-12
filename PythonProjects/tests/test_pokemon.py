import requests
import pytest

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "aec6f1e6c4e62c8ae51fdc8aec219dd6"
HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN
}
TRAINER_ID = 38084


def test_status_code():
    responce = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert responce.status_code == 200 

def test_part_of_responce():
    responce_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert responce_get.json()["data"][0]["trainer_name"] == 'Сестричка'
