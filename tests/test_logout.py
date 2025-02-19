from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators


def test_logout(browser, data):
    browser.find_element(By.XPATH, locators.logon_in_personal_account_xpath).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.logon_button_xpath)))
    browser.find_element(By.XPATH, locators.logon_email_xpath).send_keys(data["user"])
    browser.find_element(By.XPATH, locators.logon_password_xpath).send_keys(data["password"])
    browser.find_element(By.XPATH, locators.logon_button_xpath).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.logon_in_personal_account_xpath)))
    browser.find_element(By.XPATH, locators.logon_in_personal_account_xpath).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.account_button_profile)))
    browser.find_element(By.XPATH, locators.logout_button_exit_xpath).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.logon_title_xpath)))

    assert browser.find_element(By.XPATH, locators.logon_title_xpath).text == 'Вход'


