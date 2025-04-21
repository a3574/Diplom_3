import pytest
from selenium import webdriver
from objects.client import Client
import helpers as h

def create_driver(browser):
    if browser == "chrome":
        return webdriver.Chrome()
    elif browser == "firefox":
        return webdriver.Firefox()

@pytest.fixture(params=["firefox", "chrome"], autouse = True, scope = "function")
def get_driver(request): #Автоматическое открытие браузера на каждый отдельно взятый тест и закрытие после его проведения.
    driver = create_driver(request.param)
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture()
def get_client_data():
    client_name = h.get_random_name()
    client_email = h.get_random_email()
    client_password = h.get_random_password()
    client = Client(name=client_name, email=client_email, password=client_password)
    client_register_response = client.register()
    yield client
    access_token = client_register_response.json()['accessToken']
    client.delete_info(access_token).json()




