from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    def get_attribute_by_xpath_any_attribute(self, selector, name):
        return self.get_locator_by_xpath(selector).get_attribute(name)

    def get_attribute_by_class_xpath(self, selector):
        return self.get_locator_by_xpath(selector).get_attribute('class')

    def get_attribute_by_value_xpath(self, selector):
        return self.get_locator_by_xpath(selector).get_attribute('value')

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
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((self.get_locator_by_xpath(selector)))).\
            click()

    def get_element_by_attribute(self, selector, text):
        return WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element((By.XPATH, selector), text))

    def get_alert(self):
        return WebDriverWait(self.driver, 10).until(EC.alert_is_present())

    def switch_to_alert(self):
        return self.driver.switch_to.alert

    def switch_to_alert_and_fill_text(self, name):
        alert = self.driver.switch_to.alert
        alert.send_keys(name)
        alert.accept()

    def switch_to_alert_and_accept_it(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def switch_to_alert_and_decline_it(self):
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def switch_to_alert_and_return_text(self):
        alert = self.driver.switch_to.alert
        return alert.text

    def is_element_displayed(self, selector):
        try:
            if self.get_locator_by_xpath(selector):
                return True
            else:
                return False
        except NoSuchElementException:
            return False




