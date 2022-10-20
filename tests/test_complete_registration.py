from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import MainLocators, RegistrationPageLocators, LoginPageLocators, PageProfileLocators


def test_registration(driver):
    driver.find_element(*MainLocators.login_button).click()

    driver.find_element(*LoginPageLocators.registration_button).click()

    driver.find_element(*RegistrationPageLocators.name_field).send_keys('Роман')
    driver.find_element(*RegistrationPageLocators.email_field).send_keys('romantest2009@yandex.ru')
    driver.find_element(*RegistrationPageLocators.password_field).send_keys('123456')

    driver.find_element(*RegistrationPageLocators.registration_button).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//button[text()='Войти']")))

    driver.find_element(*LoginPageLocators.email_field).send_keys('romantest2009@yandex.ru')
    driver.find_element(*LoginPageLocators.password_field).send_keys('123456')

    driver.find_element(*LoginPageLocators.login_button).click()

    driver.find_element(*MainLocators.personal_account_button).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//button[text() = 'Выход']")))

    current_email = driver.find_element(*PageProfileLocators.profile_email)

    assert current_email.get_attribute('value') == 'romantest2009@yandex.ru'
