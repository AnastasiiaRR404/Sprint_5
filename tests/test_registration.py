from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from generator_login import new_email
from locators import Locators


class TestRegistration:
    def test_registration(self,driver):
        driver.find_element(*Locators.ENTER_TO_PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.AUTH_BUTTON))
        driver.find_element(*Locators.REGISTRATION_LINK).click()
        driver.find_element(*Locators.NAME_CREATED).send_keys('Анастасия')

        email = new_email()
        driver.find_element(*Locators.EMAIL_CREATED).send_keys(email)
        driver.find_element(*Locators.PASSWORD_CREATED).send_keys('123456')
        driver.find_element(*Locators.REGESTRATION_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(Locators.AUTH_BUTTON)

        )
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys('123456')
        driver.find_element(*Locators.AUTH_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            Locators.MAKE_AN_ORDER))
        text = driver.find_element(*Locators.MAKE_AN_ORDER).text

        assert text == "Оформить заказ"

    def test_password_validation(self, driver):
        driver.find_element(*Locators.ENTER_TO_PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.AUTH_BUTTON))
        driver.find_element(*Locators.REGISTRATION_LINK).click()
        driver.find_element(*Locators.NAME_CREATED).send_keys('Анастасия')

        email = new_email()
        driver.find_element(*Locators.EMAIL_CREATED).send_keys(email)
        driver.find_element(*Locators.PASSWORD_CREATED).send_keys('12345')
        driver.find_element(*Locators.REGESTRATION_BUTTON).click()

        error_message = driver.find_element(*Locators.INCORRECT_PASSWORD).text

        assert error_message == "Некорректный пароль"


