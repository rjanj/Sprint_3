import pytest
from selenium import webdriver

from tests.locators import LoginPageLocators


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")
    yield driver
    driver.quit()
