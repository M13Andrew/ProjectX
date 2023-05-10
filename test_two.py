from imports import *

class TestTwo:
    def test_three(self):
        driver_service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
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

        wait.until(ec.presence_of_element_located((By.XPATH, '//div[@class="ant-tabs-tab"][3]')))
        button_n = driver.find_element(By.XPATH, '//div[@class="ant-tabs-tab"][3]')
        button_n.click()
        time.sleep(5)





