from locators import MainLocators, PageProfileLocators


def test_rotation_from_personal_profile_to_constructor(driver):

    driver.find_element(*MainLocators.personal_account_button).click()

    driver.find_element(*PageProfileLocators.constructor_button).click()
