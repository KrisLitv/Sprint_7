import requests
import random
import string
import allure
from faker import Faker

from urls import COURIER_URL, COURIER_DELETE_URL

@allure.step('Генерируем данные для регистрации курьера')
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

@allure.step('Создаем рандомные данные для аторизации')
def get_register_payload():

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "first_name": first_name
    }

    return payload

@allure.step('Создаем нового курьера для авторизации')
def register_new_courier_and_return_login_password(payload):

    login_pass = []

    response = requests.post(COURIER_URL, data=payload)


    if response.status_code == 201:
        login_pass.append(payload['login'])
        login_pass.append(payload['password'])
        login_pass.append(payload['first_name'])

    return login_pass

@allure.step('Создаем словарь со случайно сгенерированными данными')
def build_dictionary():
    faker = Faker()
    payload = {
        "firstName": faker.first_name(),
        "lastName": faker.last_name(),
        "address": faker.text(),
        "metroStation": random.choice(range(1, 15)),
        "phone": faker.phone_number(),
        "rentTime": random.choice(range(1, 10)),
        "deliveryDate": faker.date(),
        "comment": faker.text(),
        "color": [
            "BLACK"
        ]
    }
    return payload


@allure.step('Удаляем курьера')
def delete_courier(courier_id):
    url = f"{COURIER_DELETE_URL}/{courier_id}"
    response = requests.delete(url)

    assert response.status_code == 200, f"Failed to delete courier with ID {courier_id}. Status code: {response.status_code}"

