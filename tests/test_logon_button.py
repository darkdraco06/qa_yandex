from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators


def test_button_logon_in_account(browser, data):
    browser.find_element(By.XPATH, locators.logon_in_account_button_xpath).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.logon_button_xpath)))
    browser.find_element(By.XPATH, locators.logon_email_xpath).send_keys(data["user"])
    browser.find_element(By.XPATH, locators.logon_password_xpath).send_keys(data["password"])
    browser.find_element(By.XPATH, locators.logon_button_xpath).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.logon_button_order_xpath)))

    assert browser.find_element(By.XPATH, locators.logon_button_order_xpath).text == "Оформить заказ"

def test_button_logon_register_form(browser, data):
    browser.find_element(By.XPATH, locators.logon_in_account_button_xpath).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.register_href_xpath )))
    browser.find_element(By.XPATH, locators.register_href_xpath).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.logon_in_register_form_xpath)))
    browser.find_element(By.XPATH, locators.logon_in_register_form_xpath).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.logon_button_xpath)))
    browser.find_element(By.XPATH, locators.logon_email_xpath).send_keys(data["user"])
    browser.find_element(By.XPATH, locators.logon_password_xpath).send_keys(data["password"])
    browser.find_element(By.XPATH, locators.logon_button_xpath).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.logon_button_order_xpath)))

    assert browser.find_element(By.XPATH, locators.logon_button_order_xpath).text == "Оформить заказ"

def test_button_logon_personal_account(browser,data):
    browser.find_element(By.XPATH, locators.logon_in_personal_account_xpath).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.logon_button_xpath)))
    browser.find_element(By.XPATH, locators.logon_email_xpath).send_keys(data["user"])
    browser.find_element(By.XPATH, locators.logon_password_xpath).send_keys(data["password"])
    browser.find_element(By.XPATH, locators.logon_button_xpath).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.logon_button_order_xpath)))

    assert browser.find_element(By.XPATH, locators.logon_button_order_xpath).text == "Оформить заказ"

def test_button_logon_forgot_password(browser, data):
    browser.find_element(By.XPATH, locators.logon_in_account_button_xpath).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.logon_forgot_password_xpath)))
    browser.find_element(By.XPATH, locators.logon_email_xpath).send_keys(data["user"])
    browser.find_element(By.XPATH, locators.logon_password_xpath).send_keys(data["password"])
    browser.find_element(By.XPATH, locators.logon_button_xpath).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.logon_button_order_xpath)))

    assert browser.find_element(By.XPATH, locators.logon_button_order_xpath).text == "Оформить заказ"

