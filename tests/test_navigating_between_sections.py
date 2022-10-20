from tests.locators import MainLocators


def test_navigating_between_sections(driver):
    driver.find_element(*MainLocators.element_buns).click()

    element_buns = driver.find_element(*MainLocators.element_buns)
    element_sauce = driver.find_element(*MainLocators.element_sauce)
    element_topping = driver.find_element(*MainLocators.element_topping)

    driver.execute_script("arguments[0].scrollIntoView();", element_sauce)
    element_sauce_section = driver.find_element(*MainLocators.section_sauces)
    element_sauce_is_on = element_sauce_section.get_attribute('class')

    driver.execute_script("arguments[0].scrollIntoView();", element_topping)
    element_topping_section = driver.find_element(*MainLocators.section_topping)
    element_topping_is_on = element_topping_section.get_attribute('class')

    driver.execute_script("arguments[0].scrollIntoView();", element_buns)
    element_buns_section = driver.find_element(*MainLocators.section_buns)
    element_buns_is_on = element_buns_section.get_attribute('class')

    assert element_sauce_is_on == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
    assert element_topping_is_on == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
    assert element_buns_is_on == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
