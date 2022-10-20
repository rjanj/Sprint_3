from locators import MainLocators


def test_navigating_between_profile_and_main_page_logo_click(driver):
    driver.find_element(*MainLocators.personal_account_button).click()

    driver.find_element(*MainLocators.main_logo).click()

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
