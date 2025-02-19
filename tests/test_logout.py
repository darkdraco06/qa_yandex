from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators


def test_logout(browser, data):
    browser.find_element(By.XPATH, locators.LOGON_IN_PERSONAL_ACCOUNT_XPATH).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.LOGON_BUTTON_XPATH)))
    browser.find_element(By.XPATH, locators.LOGON_EMAIL_XPATH).send_keys(data["user"])
    browser.find_element(By.XPATH, locators.LOGON_PASSWORD_XPATH).send_keys(data["password"])
    browser.find_element(By.XPATH, locators.LOGON_BUTTON_XPATH).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.LOGON_IN_PERSONAL_ACCOUNT_XPATH)))
    browser.find_element(By.XPATH, locators.LOGON_IN_PERSONAL_ACCOUNT_XPATH).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.ACCOUNT_BUTTON_PROFILE)))
    browser.find_element(By.XPATH, locators.LOGOUT_BUTTON_EXIT_XPATH).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.LOGON_TITLE_XPATH)))

    assert browser.find_element(By.XPATH, locators.LOGON_TITLE_XPATH).text == 'Вход'


