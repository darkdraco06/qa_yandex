from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators
import  time

time.sleep(10)

def test_regestration_no_name(browser,data):
    browser.find_element(By.XPATH, locators.logon_in_account_button_xpath).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.register_href_xpath)))
    browser.find_element(By.XPATH, locators.register_href_xpath).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.register_button_xpath)))
    browser.find_element(By.XPATH, locators.email_xpath).send_keys(data["random_email"])
    browser.find_element(By.XPATH, locators.password_xpath).send_keys(data["random_password"])
    browser.find_element(By.XPATH, locators.register_button_xpath).click()

    assert browser.find_element(By.XPATH, locators.register_button_xpath).text == "Зарегистрироваться"

def test_regestration_no_valid_email(browser,data):
    browser.find_element(By.XPATH, locators.logon_in_account_button_xpath).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.register_href_xpath)))
    browser.find_element(By.XPATH, locators.register_href_xpath).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.register_button_xpath)))
    browser.find_element(By.XPATH, locators.name_xpath).send_keys(data["name_user"])
    browser.find_element(By.XPATH, locators.email_xpath).send_keys(data["invalid_email"])
    browser.find_element(By.XPATH, locators.password_xpath).send_keys(data["random_password"])
    browser.find_element(By.XPATH, locators.register_button_xpath).click()

    assert browser.find_element(By.XPATH, locators.register_button_xpath).text == "Зарегистрироваться"

def test_regestration_low_password(browser, data):
    browser.find_element(By.XPATH, locators.logon_in_account_button_xpath).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.register_href_xpath)))
    browser.find_element(By.XPATH, locators.register_href_xpath).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.register_button_xpath)))
    browser.find_element(By.XPATH, locators.name_xpath).send_keys(data["name_user"])
    browser.find_element(By.XPATH, locators.email_xpath).send_keys(data["random_email"])
    browser.find_element(By.XPATH, locators.password_xpath).send_keys(data["invalid_password"])
    browser.find_element(By.XPATH, locators.register_button_xpath).click()

    assert browser.find_element(By.XPATH, locators.register_button_xpath).text == "Зарегистрироваться"

def test_regestration_error_password(browser, data):
     browser.find_element(By.XPATH, locators.logon_in_account_button_xpath).click()
     WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.logon_button_xpath)))
     browser.find_element(By.XPATH, locators.register_href_xpath).click()
     WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.register_button_xpath)))
     browser.find_element(By.XPATH, locators.password_xpath).send_keys(data["invalid_password"])
     browser.find_element(By.XPATH, locators.register_button_xpath).click()

     assert browser.find_element(By.XPATH, locators.error_message_xpath).text == "Некорректный пароль"

def test_regestration_sucsess(browser, data):
    browser.find_element(By.XPATH, locators.logon_in_account_button_xpath).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.register_href_xpath)))
    browser.find_element(By.XPATH, locators.register_href_xpath).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.register_button_xpath)))
    browser.find_element(By.XPATH, locators.name_xpath).send_keys(data["name_user"])
    browser.find_element(By.XPATH, locators.email_xpath).send_keys(data["random_email"])
    browser.find_element(By.XPATH, locators.password_xpath).send_keys(data["random_password"])
    browser.find_element(By.XPATH, locators.register_button_xpath).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.logon_title_xpath)))

    assert browser.find_element(By.XPATH, locators.logon_title_xpath).text == "Вход"