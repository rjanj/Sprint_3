from locators import MainLocators, LoginPageLocators


def test_login_from_personal_profile(driver):
    driver.find_element(*MainLocators.personal_account_button).click()

    driver.find_element(*LoginPageLocators.email_field).send_keys('romantest1996@yandex.ru')
    driver.find_element(*LoginPageLocators.password_field).send_keys('123456')

    driver.find_element(*LoginPageLocators.login_button).click()
