from locators import MainLocators


def test_navigating_between_sections(driver):

    driver.find_element(*MainLocators.section_sauces).click()

    driver.find_element(*MainLocators.section_topping).click()

    driver.find_element(*MainLocators.section_buns).click()

