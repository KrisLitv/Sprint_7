import pytest
import requests

from urls import LOGIN_URL, COURIER_URL
from helpers import register_new_courier_and_return_login_password, get_register_payload

@pytest.fixture
def new_courier():
    payload = get_register_payload()
    return register_new_courier_and_return_login_password(payload)

@pytest.fixture
def new_courier_id(new_courier):
    login, password, first_name = new_courier

    payload_login = {
        "login": login,
        "password": password
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(LOGIN_URL, data=payload_login)

    return response.json()['id']