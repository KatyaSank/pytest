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



