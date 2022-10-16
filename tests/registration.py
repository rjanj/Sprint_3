from locators import MainLocators, RegistrationPageLocators, LoginPageLocators


def test_registration(driver):
    driver.find_element(*MainLocators.login_button).click()

    driver.find_element(*LoginPageLocators.registration_button).click()

    driver.find_element(*RegistrationPageLocators.name_field).send_keys('Роман')
    driver.find_element(*RegistrationPageLocators.email_field).send_keys('romantest1996@yandex.ru')
    driver.find_element(*RegistrationPageLocators.password_field).send_keys('123456')

    driver.find_element(*RegistrationPageLocators.registration_button).click()
