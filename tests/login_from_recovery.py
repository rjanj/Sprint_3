from locators import MainLocators, LoginPageLocators, ForgotPasswordPageLocators


def test_login_from_recovery(driver):

    driver.find_element(*MainLocators.login_button).click()

    driver.find_element(*LoginPageLocators.recovery_button).click()

    driver.find_element(*ForgotPasswordPageLocators.login_button).click()

    driver.find_element(*LoginPageLocators.email_field).send_keys('romantest1996@yandex.ru')
    driver.find_element(*LoginPageLocators.password_field).send_keys('123456')

    driver.find_element(*LoginPageLocators.login_button).click()
