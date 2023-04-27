from selenium.webdriver.common.by import By
from selenium.webdriver.support import WebDriverWait
from selenium.webdriver.support.ui import Select


class Base:
    def __init__(self, driver):
        self.driver = driver

    def get_url(self, url):
        return self.driver.get(url)

    def maximize_window(self):
        return self.driver.maximize_window()

    def get_locator_by_css(self, selector):
        css = (By.CSS_SELECTOR, selector)
        return self.driver.find_element(*css)

    def get_locator_by_xpath(self, selector):
        xpath = (By.XPATH, selector)
        return self.driver.find_element(*xpath)

    def get_locator_by_id(self, selector):
        id = (By.ID, selector)
        return self.driver.find_element(*id)

    def get_locator_by_class_name(self, selector):
        class_name = (By.CLASS_NAME, selector)
        return self.driver.find_element(*class_name)

    def click_checkbox(self, selector):
        return self.get_locator_by_xpath(*selector).click

    def scroll_to_bottom(self):
        return self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def click_radio_button(self, selector):
        return self.get_locator_by_xpath(*selector).click

    def select_by_id_value(self, selector, value):
        return Select(self.get_locator_by_id(selector)).select_by_value(*value)

    def get_attribute_by_class(self, selector):
        return self.get_locator_by_id(selector).get_attribute('class')

    def get_attribute_by_value(self, selector):
        return self.get_locator_by_id(selector).get_attribute('value')

    def get_attribute_from_input(self, selector, value):
        self.get_locator_by_id(selector).send_keys(value)
        print(self.get_attribute_by_value(selector))

    def assert_that_element_is_displayed_by_css(self, selector):
        return self.get_locator_by_css(selector).is_displayed()

    def assert_that_element_is_displayed_by_xpath(self, selector):
        return self.get_locator_by_xpath(selector).is_displayed()

    def assert_that_element_is_displayed_by_id(self, selector):
        return self.get_locator_by_id(selector).is_displayed()

    def assert_that_element_is_displayed_by_class_name(self, selector):
        return self.get_locator_by_class_name(selector).is_displayed()

    def asser_that_element_is_selected_by_xpath(self, selector):
        return self.get_locator_by_xpath(selector).is_selected()

    def get_element(self, selector):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
