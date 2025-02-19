from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators


#Проверка кнопки Вход через кнопку "Войти в аккаунт"
def test_button_logon_in_account(browser, data):
    browser.find_element(By.XPATH, locators.LOGON_IN_ACCOUNT_BUTTON_XPATH).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.LOGON_BUTTON_XPATH)))
    browser.find_element(By.XPATH, locators.LOGON_EMAIL_XPATH).send_keys(data["user"])
    browser.find_element(By.XPATH, locators.LOGON_PASSWORD_XPATH).send_keys(data["password"])
    browser.find_element(By.XPATH, locators.LOGON_BUTTON_XPATH).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.LOGON_BUTTON_ORDER_XPATH)))

    assert browser.find_element(By.XPATH, locators.LOGON_BUTTON_ORDER_XPATH).text == "Оформить заказ"

#Проверка кнопки Вход через форму регистрации
def test_button_logon_register_form(browser, data):
    browser.find_element(By.XPATH, locators.LOGON_IN_ACCOUNT_BUTTON_XPATH).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.REGISTER_HREF_XPATH)))
    browser.find_element(By.XPATH, locators.REGISTER_HREF_XPATH).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.LOGON_IN_REGISTER_FORM_XPATH)))
    browser.find_element(By.XPATH, locators.LOGON_IN_REGISTER_FORM_XPATH).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.LOGON_BUTTON_XPATH)))
    browser.find_element(By.XPATH, locators.LOGON_EMAIL_XPATH).send_keys(data["user"])
    browser.find_element(By.XPATH, locators.LOGON_PASSWORD_XPATH).send_keys(data["password"])
    browser.find_element(By.XPATH, locators.LOGON_BUTTON_XPATH).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.LOGON_BUTTON_ORDER_XPATH)))

    assert browser.find_element(By.XPATH, locators.LOGON_BUTTON_ORDER_XPATH).text == "Оформить заказ"

#Проверка кнопки Вход через сслыку "Личный кабинет"
def test_button_logon_personal_account(browser,data):
    browser.find_element(By.XPATH, locators.LOGON_IN_PERSONAL_ACCOUNT_XPATH).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.LOGON_BUTTON_XPATH)))
    browser.find_element(By.XPATH, locators.LOGON_EMAIL_XPATH).send_keys(data["user"])
    browser.find_element(By.XPATH, locators.LOGON_PASSWORD_XPATH).send_keys(data["password"])
    browser.find_element(By.XPATH, locators.LOGON_BUTTON_XPATH).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.LOGON_BUTTON_ORDER_XPATH)))

    assert browser.find_element(By.XPATH, locators.LOGON_BUTTON_ORDER_XPATH).text == "Оформить заказ"

#Проверка кнопки Вход на странице Востаноления пароля
def test_button_logon_forgot_password_form(browser, data):
    browser.find_element(By.XPATH, locators.LOGON_IN_ACCOUNT_BUTTON_XPATH).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.LOGON_FORGOT_PASSWORD_XPATH)))
    browser.find_element(By.XPATH, locators.LOGON_EMAIL_XPATH).send_keys(data["user"])
    browser.find_element(By.XPATH, locators.LOGON_PASSWORD_XPATH).send_keys(data["password"])
    browser.find_element(By.XPATH, locators.LOGON_BUTTON_XPATH).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.LOGON_BUTTON_ORDER_XPATH)))

    assert browser.find_element(By.XPATH, locators.LOGON_BUTTON_ORDER_XPATH).text == "Оформить заказ"

