from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import MainLocators, LoginPageLocators, RegistrationPageLocators


def test_login_from_registration_page(driver):
    driver.find_element(*MainLocators.login_button).click()

    driver.find_element(*LoginPageLocators.registration_button).click()

    driver.find_element(*RegistrationPageLocators.login_button).click()

    driver.find_element(*LoginPageLocators.email_field).send_keys('romantest1996@yandex.ru')
    driver.find_element(*LoginPageLocators.password_field).send_keys('123456')

    driver.find_element(*LoginPageLocators.login_button).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//button[text()='Оформить заказ']")))

    order_button = driver.find_element(*MainLocators.order_button)

    assert order_button.is_displayed()
