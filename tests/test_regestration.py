from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators

def test_regestration_error_password(browser, data):
     browser.find_element(By.XPATH, locators.LOGON_IN_ACCOUNT_BUTTON_XPATH).click()
     WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.LOGON_BUTTON_XPATH)))
     browser.find_element(By.XPATH, locators.REGISTER_HREF_XPATH).click()
     WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.REGISTER_BUTTON_XPATH)))
     browser.find_element(By.XPATH, locators.PASSWORD_XPATH).send_keys(data["invalid_password"])
     browser.find_element(By.XPATH, locators.REGISTER_BUTTON_XPATH).click()

     assert browser.find_element(By.XPATH, locators.ERROR_MESSAGE_XPATH).text == "Некорректный пароль"

def test_regestration_sucsess(browser, data):
    browser.find_element(By.XPATH, locators.LOGON_IN_ACCOUNT_BUTTON_XPATH).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.REGISTER_HREF_XPATH)))
    browser.find_element(By.XPATH, locators.REGISTER_HREF_XPATH).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.REGISTER_BUTTON_XPATH)))
    browser.find_element(By.XPATH, locators.NAME_XPATH).send_keys(data["name_user"])
    browser.find_element(By.XPATH, locators.EMAIL_XPATH).send_keys(data["random_email"])
    browser.find_element(By.XPATH, locators.PASSWORD_XPATH).send_keys(data["random_password"])
    browser.find_element(By.XPATH, locators.REGISTER_BUTTON_XPATH).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.LOGON_TITLE_XPATH)))

    assert browser.find_element(By.XPATH, locators.LOGON_TITLE_XPATH).text == "Вход"