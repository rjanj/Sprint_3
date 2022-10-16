from locators import MainLocators, RegistrationPageLocators, LoginPageLocators


def test_wrong_registration_password_shows_error(driver):
    driver.find_element(*MainLocators.login_button).click()

    driver.find_element(*LoginPageLocators.registration_button).click()

    driver.find_element(*RegistrationPageLocators.name_field).send_keys('Роман')
    driver.find_element(*RegistrationPageLocators.email_field).send_keys('romantest1996@yandex.ru')
    driver.find_element(*RegistrationPageLocators.password_field).send_keys('123')

    driver.find_element(*RegistrationPageLocators.registration_button).click()

    text_error = driver.find_element(*RegistrationPageLocators.password_error)

    assert text_error.text == 'Некорректный пароль'

