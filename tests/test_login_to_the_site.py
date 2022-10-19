from selenium.webdriver.common.by import By
from locators import MainLocators, LoginPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_login_to_the_site(driver):
    driver.find_element(*MainLocators.login_button).click()

    driver.find_element(*LoginPageLocators.email_field).send_keys('romantest1996@yandex.ru')
    driver.find_element(*LoginPageLocators.password_field).send_keys('123456')

    driver.find_element(*LoginPageLocators.login_button).click()

    driver.find_element(*MainLocators.personal_account_button).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//button[text() = 'Выход']")))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'


