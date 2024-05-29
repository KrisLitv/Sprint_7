import requests
import allure

from urls import COURIER_URL
from helpers import register_new_courier_and_return_login_password, generate_random_string, get_register_payload


class TestCreateCourier:

    @allure.title('Проверка кода API создания курьера')
    def test_create_code(self):
        login, password, first_name = generate_random_string(10), generate_random_string(10), generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post(COURIER_URL, json=payload)
        assert response.status_code == 201
        response_data = response.json()

        assert 'ok' in response_data and response_data['ok'] is True, "Ответ не содержит ключ 'ok' с True значением"


    @allure.title('Проверка тела API создания курьера')
    def test_create_body(self):
        login, password, first_name = generate_random_string(10), generate_random_string(10), generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(COURIER_URL, json=payload)
        response_data = response.json()
        assert response_data.get('ok'), "Ошибка: 'ok' отсутствует в ответе"



    @allure.title('Проверка кода API на создания дублирующегося курьера')
    def test_create_duplicate_code(self):
        register_payload = get_register_payload()
        login, password, first_name = register_new_courier_and_return_login_password(register_payload)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(COURIER_URL, json=payload)
        assert response.status_code == 409, f"Ошибка: ожидался код 409, получен {response.status_code}"

    @allure.title('Проверка тела API создания дублирующегося курьера')
    def test_create_duplicate_body(self):
        register_payload = get_register_payload()
        login, password, first_name = register_new_courier_and_return_login_password(register_payload)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(COURIER_URL, json=payload)
        response_data = response.json()
        expected_message = 'Этот логин уже используется. Попробуйте другой.'
        assert response_data.get('message') == expected_message, f"Ошибка: ожидалось сообщение '{expected_message}', получено {response_data.get('message')}"

    @allure.title('Проверка кода API на обязательные поля при создании курьера')
    def test_create_required_fields_code(self):
        login = generate_random_string(10)

        payload = {
            "login": login
        }

        response = requests.post(COURIER_URL, json=payload)
        assert response.status_code == 400, f"Ошибка: ожидался код 400, получен {response.status_code}"

    @allure.title('Проверка тела API на обязательные поля при создании курьера')
    def test_create_required_fields_body(self):
        login = generate_random_string(10)

        payload = {
            "login": login
        }

        response = requests.post(COURIER_URL, json=payload)
        response_data = response.json()
        expected_message = 'Недостаточно данных для создания учетной записи'
        assert response_data.get('message') == expected_message, f"Ошибка: ожидалось сообщение '{expected_message}', получено {response_data.get('message')}"