from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
from constants import Constant

class TestLogout:
    def test_logout(self,driver):
        driver.find_element(*Locators.ENTER_TO_PROFILE_BUTTON).click() #переход по клику на «Личный кабинет».


        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.EMAIL_INPUT))

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Constant.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constant.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.PROFILE)).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            Locators.EXIT)).click()


        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            Locators.AUTH_BUTTON))

        text = driver.find_element(*Locators.AUTH_BUTTON).text
        assert text == "Войти"