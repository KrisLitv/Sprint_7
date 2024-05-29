import requests
import allure

from urls import LOGIN_URL
from helpers import generate_random_string


class TestLogin:
    @allure.title('Проверка кода API на успешную авторизации')
    def test_success_login_code(self, new_courier):
        login, password, first_name = new_courier

        payload = {
            "login": login,
            "password": password
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post(LOGIN_URL, data=payload)
        assert response.status_code == 200

    @allure.title('Проверка тела API на успешную авторизации')
    def test_success_login_body(self, new_courier):
        login, password, first_name = new_courier

        payload = {
            "login": login,
            "password": password
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post(LOGIN_URL, data=payload)
        assert isinstance(response.json().get('id'), int)

    @allure.title('Проверка тела API на ошибку авторизации при наличии только поля логин')
    def test_error_only_login_body(self, new_courier):
        login, password, first_name = new_courier

        payload = {
            "login": login
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post(LOGIN_URL, data=payload)
        assert response.json()['message'] == 'Недостаточно данных для входа'

    @allure.title('Проверка кода API на ошибку авторизации при наличии только поля логин')
    def test_error_only_login_code(self, new_courier):
        login, password, first_name = new_courier

        payload = {
            "login": login
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post(LOGIN_URL, data=payload)
        assert response.status_code == 400
        # 504 выдаёт

    @allure.title('Проверка тела API на ошибку авторизации при наличии только поля пароль')
    def test_error_only_password_body(self, new_courier):
        login, password, first_name = new_courier

        payload = {
            "password": password
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post(LOGIN_URL, data=payload)
        assert response.json()['message'] == 'Недостаточно данных для входа'

    @allure.title('Проверка кода API на ошибку авторизации при наличии только поля пароль')
    def test_error_only_password_code(self, new_courier):
        login, password, first_name = new_courier

        payload = {
            "password": password
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post(LOGIN_URL, data=payload)
        assert response.status_code == 400

    @allure.title('Проверка кода API на ошибку авторизации при не зарегестрированном курьере')
    def test_unregistered_login_password_code(self):
        login, password = generate_random_string(10), generate_random_string(10)

        payload = {
            'login': login,
            "password": password
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post(LOGIN_URL, data=payload)
        assert response.status_code == 404

    @allure.title('Проверка тела API на ошибку авторизации при не зарегистрированном курьере')
    def test_unregistered_login_password_body(self):
        login, password = generate_random_string(10), generate_random_string(10)

        payload = {
            'login': login,
            "password": password
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post(LOGIN_URL, data=payload)
        assert response.json()['message'] == 'Учетная запись не найдена'

    @allure.title('Проверка кода API на ошибку авторизации при неправильном пароле')
    def test_wrong_login_password_code(self, new_courier):
        fake_password = generate_random_string(10)
        login, password, first_name = new_courier

        payload = {
            'login': login,
            "password": fake_password
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post(LOGIN_URL, data=payload)
        assert response.status_code == 404

    @allure.title('Проверка тело API на ошибку авторизации при неправильном пароле')
    def test_wrong_login_password_body(self, new_courier):
        fake_password = generate_random_string(10)
        login, password, first_name = new_courier

        payload = {
            'login': login,
            "password": fake_password
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post(LOGIN_URL, data=payload)
        assert response.json()['message'] == 'Учетная запись не найдена'


