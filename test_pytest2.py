import urllib.request
from Base import Base


def test_find_bbc_element_by_xpath(driver):
    base = Base(driver)
    base.get_url('https://www.bbc.com/news')
    base.get_locator_by_xpath("//div[contains(@class, '@m gel-2/3@m gs')]")
    assert base.assert_that_element_is_displayed_by_xpath("//div[contains(@class, '@m gel-2/3@m gs')]")


def test_find_bbc_element_by_css(driver):
    base = Base(driver)
    base.get_url('https://www.bbc.com/news')
    base.get_locator_by_css("div[class*='@m gel-2/3@m gs']")
    assert base.assert_that_element_is_displayed_by_css("div[class*='@m gel-2/3@m gs']")


def test_find_bbc_logo_by_xpath(driver):
    base = Base(driver)
    base.get_url('https://www.bbc.com/news')
    base.get_locator_by_xpath("//a[@id='homepage-link']")
    assert base.assert_that_element_is_displayed_by_xpath("//a[@id='homepage-link']")


def test_find_bbc_logo_by_css(driver):
    base = Base(driver)
    base.get_url('https://www.bbc.com/news')
    base.get_locator_by_css("#homepage-link")
    assert base.assert_that_element_is_displayed_by_css('#homepage-link')


def test_find_bbc_sport_title_by_xpath(driver):
    base = Base(driver)
    base.get_url('https://www.bbc.com/news')
    base.get_locator_by_xpath("//nav[contains(@class,'international')]/ul/li[3]")
    assert base.assert_that_element_is_displayed_by_xpath("//nav[contains(@class,'international')]/ul/li[3]")


def test_find_bbc_sport_title_by_css(driver):
    base = Base(driver)
    base.get_url('https://www.bbc.com/news')
    base.get_locator_by_css("nav.orbit-header-links.international>ul>li.orb-nav-sport")
    assert base.assert_that_element_is_displayed_by_css("nav.orbit-header-links.international>ul>li.orb-nav-sport")


def test_alert(driver):
    base = Base(driver)
    base.get_url('https://learn.javascript.ru/task/simple-page')
    base.get_locator_by_xpath('/html/body/div[1]/div[2]/div/main/div[2]/div[2]/div[2]/div[1]/p[2]/a').click()
    base.switch_to_alert_and_fill_text("Katya")
    assert base.switch_to_alert_and_return_text() == "Katya"


def test_new_window(driver):
    base = Base(driver)
    base.get_url('http://the-internet.herokuapp.com/windows')
    main_window = driver.current_window_handle
    base.get_locator_by_xpath('//*[@id="content"]/div/a').click()
    new_window = [window for window in driver.window_handles if
                  window != main_window][0]
    driver.switch_to.window(new_window)
    assert base.get_locator_by_xpath('/html/body/div/h3').text == "New Window"


def test_iframe(driver):
    base = Base(driver)
    base.get_url('http://the-internet.herokuapp.com/iframe')
    driver.switch_to.frame(base.get_locator_by_xpath('//*[@id="mce_0_ifr"]'))
    assert base.get_locator_by_xpath('//*[@id="tinymce"]/p').text == 'Your content goes here.'


def test_dynamic_controls(driver):
    base = Base(driver)
    base.get_url('http://the-internet.herokuapp.com/dynamic_controls')
    base.get_locator_by_xpath('//*[@id="checkbox"]/input').click()
    assert base.asser_that_element_is_selected_by_xpath('//*[@id="checkbox"]/input')
    base.get_locator_by_xpath('//*[@id="checkbox-example"]/button').click()
    base.get_element_by_attribute('//*[@id="checkbox-example"]/button', "Add")
    assert base.get_locator_by_xpath('//*[@id="message"]').text == "It's gone!"
    assert not base.is_element_displayed('//*[@id="checkbox"]/input')
    assert not base.get_locator_by_xpath('//*[@id="input-example"]/input').is_enabled()
    base.get_locator_by_xpath('//*[@id="input-example"]/button').click()
    base.get_element_by_attribute('//*[@id="message"]', "It's enabled!")
    assert base.get_locator_by_xpath('//*[@id="input-example"]/input').is_enabled()


def test_download_file(driver):
    base = Base(driver)
    base.get_url('http://the-internet.herokuapp.com/download')
    response = urllib.request.urlopen('http://the-internet.herokuapp.com/download/empty.txt')
    assert response.read() == b'not empty!'


def test_upload_file(driver):
    base = Base(driver)
    base.get_url('http://the-internet.herokuapp.com/upload')
    file_path = "C:/Users/Admin/Desktop/Python/pytest/Photo.png"
    base.get_locator_by_xpath('//*[@id="file-upload"]').send_keys(file_path)
    base.get_locator_by_xpath('//*[@id="file-submit"]').click()
    assert base.assert_that_element_is_displayed_by_xpath('//*[@id="uploaded-files"]')
