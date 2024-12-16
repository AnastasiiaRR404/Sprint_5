
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
from constants import Constant

class TestLogin:
    def test_login(self,driver):
        driver.find_element(*Locators.ENTER_TO_PROFILE_BUTTON).click() #переход по клику на «Личный кабинет».


        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.EMAIL_INPUT))

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Constant.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constant.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            Locators.MAKE_AN_ORDER))
        text = driver.find_element(*Locators.MAKE_AN_ORDER).text
        assert text == "Оформить заказ"

    def test_login_profile(self,driver):
        driver.find_element(*Locators.PROFILE).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Constant.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constant.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            Locators.MAKE_AN_ORDER))
        text = driver.find_element(*Locators.MAKE_AN_ORDER).text
        assert text == "Оформить заказ"

    def test_login_through_registration (self,driver):
        driver.find_element(*Locators.ENTER_TO_PROFILE_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(Locators.AUTH_BUTTON)

        )
        driver.find_element(*Locators.REGISTRATION_LINK).click()
        driver.find_element(*Locators.LOGIN).click()


        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Constant.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constant.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            Locators.MAKE_AN_ORDER))
        text = driver.find_element(*Locators.MAKE_AN_ORDER).text
        assert text == "Оформить заказ"

    def test_login_through_password_restore (self,driver):
        driver.find_element(*Locators.ENTER_TO_PROFILE_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(Locators.AUTH_BUTTON)

        )
        driver.find_element(*Locators.RESTORE_LINK).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Constant.EMAIL)
        driver.find_element(*Locators.RESTORE_BUTTON).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.staleness_of(driver.find_element(*Locators.LOGIN)))

        driver.find_element(*Locators.LOGIN).click()

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Constant.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constant.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            Locators.MAKE_AN_ORDER))
        text = driver.find_element(*Locators.MAKE_AN_ORDER).text
        assert text == "Оформить заказ"




