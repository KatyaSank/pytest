from Base import Base


def test_text_box(driver):
    base = Base(driver)
    base.get_url('https://demoqa.com/text-box')
    base.maximize_window()
    base.get_locator_by_id('userName').send_keys("Kate Sankovich")
    base.get_locator_by_id('userEmail').send_keys("Kate@gmail.com")
    base.get_locator_by_id('currentAddress').send_keys("Klaipeda")
    base.get_locator_by_id('permanentAddress').send_keys("World")
    base.scroll_to_bottom()
    base.get_locator_by_id('submit').click()
    driver.save_screenshot('test.png')
    assert base.assert_that_element_is_displayed_by_id('name')
    assert base.assert_that_element_is_displayed_by_id('email')
    assert base.assert_that_element_is_displayed_by_id('currentAddress')
    assert base.assert_that_element_is_displayed_by_id('permanentAddress')


def test_checkbox(driver):
    base = Base(driver)
    base.get_url("https://demoqa.com/checkbox")
    base.maximize_window()
    base.get_locator_by_class_name('rct-icon').click()
    base.get_locator_by_xpath('//span[text()="Office"]').click()
    assert base.assert_that_element_is_displayed_by_xpath('//span[text()="office"]')
    assert base.assert_that_element_is_displayed_by_xpath('//span[text()="public"]')
    assert base.assert_that_element_is_displayed_by_xpath('//span[text()="private"]')
    assert base.assert_that_element_is_displayed_by_xpath('//span[text()="classified"]')
    assert base.assert_that_element_is_displayed_by_xpath('//span[text()="general"]')


def test_radio(driver):
    base = Base(driver)
    base.get_url("https://demoqa.com/radio-button")
    base.maximize_window()
    base.get_locator_by_xpath('//label[@for="impressiveRadio"]').click()
    assert base.assert_that_element_is_displayed_by_xpath('//span[text()="Impressive"]')


def test_add_table(driver):
    base = Base(driver)
    base.get_url("https://demoqa.com/webtables")
    base.maximize_window()
    base.get_locator_by_id('addNewRecordButton').click()
    base.get_attribute_from_input('firstName', "Katie")
    base.get_attribute_from_input('lastName', "Sankovich")
    base.get_attribute_from_input('userEmail', "Katya@gmail.com")
    base.get_attribute_from_input('age', "99")
    base.get_attribute_from_input('salary', "999")
    base.get_attribute_from_input('department', "QA")
    assert base.get_attribute_by_value('firstName') == "Katie"
    assert base.get_attribute_by_value('lastName') == "Sankovich"
    assert base.get_attribute_by_value('userEmail') == "Katya@gmail.com"
    assert base.get_attribute_by_value('age') == "99"
    assert base.get_attribute_by_value('salary') == "999"
    assert base.get_attribute_by_value('department') == "QA"
    base.get_locator_by_id('submit').click()
    assert base.assert_that_element_is_displayed_by_xpath('//div[text()="Katya@gmail.com"]')


def test_update_table(driver):
    base = Base(driver)
    base.get_url("https://demoqa.com/webtables")
    base.maximize_window()
    base.get_locator_by_id('addNewRecordButton').click()
    base.get_locator_by_id('firstName').send_keys("Katie")
    base.get_locator_by_id('lastName').send_keys("Sankovich")
    base.get_locator_by_id('userEmail').send_keys("Katya@gmail.com")
    base.get_locator_by_id('age').send_keys("99")
    base.get_locator_by_id('salary').send_keys("999")
    base.get_locator_by_id('department').send_keys("QA")
    base.get_locator_by_id('submit').click()
    assert base.assert_that_element_is_displayed_by_xpath('//div[text()="Katya@gmail.com"]')
    base.get_locator_by_xpath('//*[@id="edit-record-4"]').click()
    base.get_locator_by_id('age').clear()
    base.get_locator_by_id('age').send_keys("0")
    base.get_locator_by_id('firstName').clear()
    base.get_locator_by_id('firstName').send_keys("S")
    print(base.get_attribute_by_class('submit'))
    base.get_locator_by_id('submit').click()
    new_age = base.get_locator_by_xpath('//div[text()="0"]').text
    new_name = base.get_locator_by_xpath('//div[text()="S"]').text
    assert new_age == "0"
    assert new_name == "S"


def test_dropdown(driver):
    base = Base(driver)
    base.get_url("https://demoqa.com/select-menu")
    base.maximize_window()
    base.select_by_id_value('oldSelectMenu', '7')
    assert base.asser_that_element_is_selected_by_xpath('//*[@id="oldSelectMenu"]/option[8]')
