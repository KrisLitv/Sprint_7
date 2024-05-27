import pytest
import requests
import allure
from urls import color_order_data, ORDER_URL
from helpers import build_dictionary


class TestLogin:


    @pytest.mark.parametrize('color',
                             color_order_data)
    @allure.title('Проверка разных выборов цвета')
    def test_success_create_order_color(self, color):
        payload = build_dictionary()
        payload['color'] = color
        response = requests.post(ORDER_URL, data=payload)
        assert response.status_code == 201
        # {'code': 500, 'message': 'values.map is not a function'}

    @allure.title('Проверка ответа API на получение id после авторизации')
    def test_success_create_order_track_in_body(self):
        payload = build_dictionary()
        payload['color'] = []
        response = requests.post(ORDER_URL, data=payload)
        assert response.json().get('track')