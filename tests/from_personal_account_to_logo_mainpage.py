from locators import MainLocators


def test_personal_profile(driver):

    driver.find_element(*MainLocators.personal_account_button).click()

    driver.find_element(*MainLocators.main_logo).click()
