import pytest
from selenium import webdriver
import random
import re

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()

@pytest.fixture
def data():
    return {
        "password": "EWfZ3cJFKPw",
        "user": "SergeyZ18006@ya.ru",
        "invalid_password": "12345",
        "name_user": "Tester Tosterov",
        "random_email": f"Test_Testov_18_{random.randint(100, 999)}@test.ru",
        "invalid_email": "no_time_to_cry.ru6",
        "random_password": f"{random.randint(100000, 9999999)}"
    }