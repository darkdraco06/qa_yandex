from selenium.webdriver.common.by import By
import locators


def test_builder_go_to_fillings(browser):
    browser.find_element(By.XPATH, locators.builder_fillings_xpath).click()
    assert browser.find_element(By.XPATH, locators.builder_fillings_active_xpath).text == "Начинки"

def test_builder_go_to_sauces(browser):
    browser.find_element(By.XPATH, locators.builder_sauces_xpath).click()
    assert browser.find_element(By.XPATH, locators.builder_sauces_active_xpath).text == "Соусы"

def test_builder_go_to_buns(browser):
    browser.find_element(By.XPATH, locators.builder_sauces_xpath).click()
    browser.find_element(By.XPATH, locators.builder_buns_xpath).click()
    assert browser.find_element(By.XPATH, locators.builder_buns_active_xpath).text == "Булки"
