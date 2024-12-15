from constants import Constant
from locators import Locators

class TestTransitionsFromTheConstructor:
    def test_sauses_from_the_constructor(self,driver):

        driver.find_element(*Locators.SAUCES).click()

        actual_class = driver.find_element(*Locators.SAUCES).get_attribute("class")
        assert actual_class == Constant.EXPECTED_CLASS

    def test_toppings_from_the_constructor(self,driver):

        driver.find_element(*Locators.TOPPINGS).click()
        actual_class = driver.find_element(*Locators.TOPPINGS).get_attribute("class")
        assert actual_class == Constant.EXPECTED_CLASS

    def test_buns_from_the_constructor(self,driver):

        driver.find_element(*Locators.SAUCES).click()
        driver.find_element(*Locators.BUNS).click()
        actual_class = driver.find_element(*Locators.BUNS).get_attribute("class")
        assert actual_class == Constant.EXPECTED_CLASS