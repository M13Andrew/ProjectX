from imports import *

class TestTwo:
    def login(self):
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.maximize_window()
        driver.get('https://bes.datawiz.io/login/')
        wait = WebDriverWait(driver, 15, 0.3)
        wait.until(ec.visibility_of_element_located((By.ID, "id_auth-username")))
        login = driver.find_element(By.ID, "id_auth-username")
        login.send_keys('andrew.masyuk@datawiz.io')
        password = driver.find_element(By.ID, "id_auth-password")
        password.send_keys('Qweasd2zxc')
        button = driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block']")
        button.click()

    def test_three(self):
        # self.login()
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.maximize_window()
        driver.get('https://bes.datawiz.io/login/')
        wait = WebDriverWait(driver, 15, 0.3)
        wait.until(ec.visibility_of_element_located((By.ID, "id_auth-username")))
        login = driver.find_element(By.ID, "id_auth-username")
        login.send_keys('andrew.masyuk@datawiz.io')
        password = driver.find_element(By.ID, "id_auth-password")
        password.send_keys('Qweasd2zxc')
        button = driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block']")
        button.click()

        wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='ant-select-selector']")))
        dropdown = driver.find_elements(By.XPATH, "//div[@class='ant-select-selector']")
        dropdown[0].click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='ant-select-item-option-content']")))
        item_button = driver.find_elements(By.XPATH, "//div[@class='ant-select-item-option-content']")
        item_button[1].click()
        button_go = driver.find_elements(By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-block dw-btn']")
        button_go[0].click()

        driver.switch_to.window(driver.window_handles[1])

        last_ninety_days_button = wait.until(ec.presence_of_element_located((By.XPATH, '//div[@class="ant-tabs-tab"][3]')))
        # wait.until(ec.presence_of_element_located((By.XPATH, '//div[@class="ant-tabs-tab"][3]')))
        # last_ninety_days_button = driver.find_element(By.XPATH, '//div[@class="ant-tabs-tab"][3]')
        last_ninety_days_button.click()

        plan_by_sells_qty_button = driver.find_element(By.XPATH, "//label[@class='ant-radio-button-wrapper'][1]")
        plan_by_sells_qty_button.click()

        plan_by_profit_button = driver.find_element(By.XPATH, "//label[@class='ant-radio-button-wrapper'][2]")
        plan_by_profit_button.click()

        plan_by_seles_button = driver.find_element(By.XPATH, "//label[@class='ant-radio-button-wrapper']")
        plan_by_seles_button.click()

        time.sleep(5)







