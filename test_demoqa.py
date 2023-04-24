from selenium.webdriver.common.by import By


def test_text_box(driver):
    driver.get('https://demoqa.com/text-box')
    driver.maximize_window()
    driver.find_element(By.ID, 'userName').send_keys("Kate Sankovich")
    driver.find_element(By.ID, 'userEmail').send_keys("Kate@gmail.com")
    driver.find_element(By.ID, 'currentAddress').send_keys("Klaipeda")
    driver.find_element(By.ID, 'permanentAddress').send_keys("World")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.find_element(By.ID, 'submit').click()
    name = driver.find_element(By.ID, 'name')
    email = driver.find_element(By.ID, 'email')
    c_address = driver.find_element(By.ID, 'currentAddress')
    p_address = driver.find_element(By.ID, 'permanentAddress')
    assert name.is_displayed()
    assert email.is_displayed()
    assert c_address.is_displayed()
    assert p_address.is_displayed()


def test_checkbox(driver):
    driver.get("https://demoqa.com/checkbox")
    driver.maximize_window()
    driver.find_element(By.CLASS_NAME, 'rct-icon').click()
    driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/span/label/span[3]').click()
    office = driver.find_element(By.XPATH, '//*[@id="result"]/span[2]')
    public = driver.find_element(By.XPATH, '//*[@id="result"]/span[3]')
    private = driver.find_element(By.XPATH, '//*[@id="result"]/span[4]')
    classified = driver.find_element(By.XPATH, '//*[@id="result"]/span[5]')
    general = driver.find_element(By.XPATH, '//*[@id="result"]/span[6]')
    assert office.is_displayed()
    assert public.is_displayed()
    assert private.is_displayed()
    assert classified.is_displayed()
    assert general.is_displayed()


def test_radio(driver):
    driver.get("https://demoqa.com/radio-button")
    driver.maximize_window()
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/label').click()
    impressive = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/p/span')
    assert impressive.is_displayed()


def test_add_table(driver):
    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()
    driver.find_element(By.ID, 'addNewRecordButton').click()
    driver.find_element(By.ID, 'firstName').send_keys("Katie")
    driver.find_element(By.ID, 'lastName').send_keys("Sankovich")
    driver.find_element(By.ID, 'userEmail').send_keys("Katya@gmail.com")
    driver.find_element(By.ID, 'age').send_keys("99")
    driver.find_element(By.ID, 'salary').send_keys("999")
    driver.find_element(By.ID, 'department').send_keys("QA")
    driver.find_element(By.ID, 'submit').click()
    new_line = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]')
    assert new_line.is_displayed()


def test_update_table(driver):
    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()
    driver.find_element(By.ID, 'addNewRecordButton').click()
    driver.find_element(By.ID, 'firstName').send_keys("Katie")
    driver.find_element(By.ID, 'lastName').send_keys("Sankovich")
    driver.find_element(By.ID, 'userEmail').send_keys("Katya@gmail.com")
    driver.find_element(By.ID, 'age').send_keys("99")
    driver.find_element(By.ID, 'salary').send_keys("999")
    driver.find_element(By.ID, 'department').send_keys("QA")
    driver.find_element(By.ID, 'submit').click()
    new_line = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]')
    assert new_line.is_displayed()
    driver.find_element(By.XPATH, '//*[@id="edit-record-4"]').click()
    driver.find_element(By.ID, 'age').clear()
    driver.find_element(By.ID, 'age').send_keys("0")
    driver.find_element(By.ID, 'firstName').clear()
    driver.find_element(By.ID, 'firstName').send_keys("S")
    driver.find_element(By.ID, 'submit').click()
    new_age = driver.find_element(By.XPATH,
                                  '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[3]'). \
        text
    new_name = driver.find_element(By.XPATH,
                                   '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[1]'). \
        text
    assert new_age == "0"
    assert new_name == "S"
