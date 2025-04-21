import requests
import allure
from urls import CLIENT_REGISTER, CLIENT_INFO


class Client:
    def __init__(self, email=None, name=None, password=None):
        self.email = email
        self.name = name
        self.password = password

    @allure.step('Создание пользователя через post запрос.')
    def register(self):
        params = {}
        if self.email:
            params['email'] = self.email
        if self.name:
            params['name'] = self.name
        if self.password:
            params['password'] = self.password
        responce_register = requests.post(url=CLIENT_REGISTER, data=params)
        return responce_register


    @allure.step('Удаление информации о пользователе через delete запрос')
    def delete_info(self, authorization=None):
        headers = {}
        if authorization:
            headers['authorization'] = authorization
        responce_delete_info = requests.delete(url=CLIENT_INFO, headers=headers)
        return responce_delete_info




