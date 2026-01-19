from locators import MainPageLocators
from urls import URLS

class TestConstructorPage:

    def test_transition_to_bun_success(self, driver):
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.sauces_btn).click() # Кликаем на "Соусы" для сброса состояния
        driver.find_element(*MainPageLocators.bun_btn).click() # Кликаем на "Булки"

        bun_tab_class = driver.find_element(*MainPageLocators.bun_btn).get_attribute("class") # Получаем значение атрибута class у таба "Булки"
        assert "tab_tab_type_current" in bun_tab_class # Проверяем, что класс содержит "tab_tab_type_current", обозначающий активный таб

    def test_transition_to_sauces_success(self, driver):
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.sauces_btn).click() # Кликаем на "Соусы"

        sauces_tab_class = driver.find_element(*MainPageLocators.sauces_btn).get_attribute("class") # Получаем значение атрибута class у таба "Соусы"
        assert "tab_tab_type_current" in sauces_tab_class # Проверяем, что класс содержит "tab_tab_type_current", обозначающий активный таб

    def test_transition_to_topping_success(self, driver):
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.toppings_btn).click() # Кликаем на "Начинки"

        topping_tab_class = driver.find_element(*MainPageLocators.toppings_btn).get_attribute("class") # Получаем значение атрибута class у таба "Начинки"
        assert "tab_tab_type_current" in topping_tab_class # Проверяем, что класс содержит "tab_tab_type_current", обозначающий активный таб
