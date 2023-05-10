from imports import *

class TestTwo:
    # def login(self):
    #     driver_service = Service(ChromeDriverManager().install())
    #     options = webdriver.ChromeOptions()
    #     driver = webdriver.Chrome(service=driver_service)
    #     driver.maximize_window()
    #     driver.get('https://bes.datawiz.io/login/')
    #     # wait = WebDriverWait(driver, 15, 0.3)
    #     # wait.until(ec.visibility_of_element_located((By.ID, "id_auth-username")))
    #     login = driver.find_element(By.ID, "id_auth-username")
    #     login.send_keys('andrew.masyuk@datawiz.io')
    #     password = driver.find_element(By.ID, "id_auth-password")
    #     password.send_keys('Qweasd2zxc')
    #     button = driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block']")
    #     button.click()

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
        item = driver.find_elements(By.XPATH, "//div[@class='ant-select-item-option-content']")
        item[1].click()
        button_go = driver.find_elements(By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-block dw-btn']")
        button_go[0].click()
        # time.sleep(5)

        driver.switch_to.window(driver.window_handles[1])
        # time.sleep(5)

        button_n = wait.until(ec.presence_of_element_located((By.XPATH, '//div[@class="ant-tabs-tab"][3]')))
        # wait.until(ec.presence_of_element_located((By.XPATH, '//div[@class="ant-tabs-tab"][3]')))
        # button_n = driver.find_element(By.XPATH, '//div[@class="ant-tabs-tab"][3]')
        button_n.click()

        plan_button = driver.find_element(By.XPATH, "//label[@class='ant-radio-button-wrapper'][2]")
        plan_button.click()

        time.sleep(5)







