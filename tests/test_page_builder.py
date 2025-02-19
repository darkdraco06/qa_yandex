from selenium.webdriver.common.by import By
import locators


def test_builder_go_to_fillings(browser):
    browser.find_element(By.XPATH, locators.BUILDER_FILLINGS_XPATH).click()
    assert browser.find_element(By.XPATH, locators.BUILDER_FILLINGS_ACTIVE_XPATH).text == "Начинки"

def test_builder_go_to_sauces(browser):
    browser.find_element(By.XPATH, locators.BUILDER_SAUCES_XPATH).click()
    assert browser.find_element(By.XPATH, locators.BUILDER_SAUCES_ACTIVE_XPATH).text == "Соусы"

def test_builder_go_to_buns(browser):
    browser.find_element(By.XPATH, locators.BUILDER_SAUCES_XPATH).click()
    browser.find_element(By.XPATH, locators.BUILDER_BUNS_XPATH).click()
    assert browser.find_element(By.XPATH, locators.BUILDER_BUNS_ACTIVE_XPATH).text == "Булки"
