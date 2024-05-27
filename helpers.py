import requests
import random
import string

from faker import Faker

from urls import COURIER_URL


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

def get_register_payload():

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    return payload

def register_new_courier_and_return_login_password(payload):

    login_pass = []

    response = requests.post(COURIER_URL, data=payload)

    if response.status_code == 201:
        login_pass.append(payload['login'])
        login_pass.append(payload['password'])
        login_pass.append(payload['first_name'])

    return login_pass


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
