from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators


def test_from_personal_account_go_to_logo(browser):
    browser.find_element(By.XPATH, locators.logon_in_personal_account_xpath).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.logon_button_xpath)))
    browser.find_element(By.XPATH, locators.builder_logo_xpath).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.builder_make_burger_xpath)))

    assert browser.find_element(By.XPATH, locators.builder_make_burger_xpath).text == 'Соберите бургер'

