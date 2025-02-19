from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators


def test_from_personal_account_go_to_logo(browser):
    browser.find_element(By.XPATH, locators.LOGON_IN_PERSONAL_ACCOUNT_XPATH).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.LOGON_BUTTON_XPATH)))
    browser.find_element(By.XPATH, locators.BUILDER_LOGO_XPATH).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.BUILDER_MAKE_BURGER_XPATH)))

    assert browser.find_element(By.XPATH, locators.BUILDER_MAKE_BURGER_XPATH).text == 'Соберите бургер'

