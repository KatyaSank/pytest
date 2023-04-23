from selenium.webdriver.common.by import By


def test_first(driver):
    driver.get('https://www.21vek.by/')

    # driver.add_cookie({'name': 'clickanalyticsresource', 'value': '673cbf00-c9c8-421a-8a52-973ea7b59bf5'})
    # driver.delete_cookie('clickanalyticsresource')
    # driver.delete_all_cookies()

    driver.execute_script("document.getElementById('modal-cookie').style.display =  'none'")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    sel = driver.find_element(By.XPATH, '//*[@id="footer-inner"]/div/div/div[2]/div/a[2]')
    assert sel.is_displayed()

    # logo_xpath = '//*[@id="header"]/div/div[4]/div/div/ul/li[4]'
    # logo_locator = driver.find_element(By.XPATH, logo_xpath)
    # logo_locator.click()
    # current_url = driver.current_url
    # assert current_url == 'https://www.21vek.by/refrigerators/'

# def test_delivery_firefox():
#     s = Service(executable_path=GeckoDriverManager().install())
#     driver = webdriver.Firefox(service=s)
#
#     driver.get('https://www.21vek.by/')
#     driver.fullscreen_window()
#
#     driver.close()
#     driver.quit()
