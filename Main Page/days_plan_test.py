from imports import *

class TestDays:
    def __init__(self):
        self.driver_service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.wait = WebDriverWait(self.driver, 15, 0.3)

    def click_button(self, by, path):
        button = self.driver.find_element(by, path)
        button.click()
        time.sleep(1)

    def login(self, login, password):
        self.driver.maximize_window()
        self.driver.get('https://bes.datawiz.io/login/')
        self.wait.until(ec.visibility_of_element_located((By.ID, 'id_auth-username')))
        login_input = self.driver.find_element(By.ID, 'id_auth-username')
        login_input.send_keys(login)
        password_input = self.driver.find_element(By.ID, 'id_auth-password')
        password_input.send_keys(password)
        button = self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block']")
        button.click()

    def clean(self):
        self.login('andrew.masyuk@datawiz.io', 'Qweasd2zxc')

        self.wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='ant-select-selector']")))
        dropdown = self.driver.find_elements(By.XPATH, "//div[@class='ant-select-selector']")
        dropdown[0].click()
        self.wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='ant-select-item-option-content']")))
        item_button = self.driver.find_elements(By.XPATH, "//div[@class='ant-select-item-option-content']")
        item_button[1].click()
        button_go = self.driver.find_elements(By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-block dw-btn']")
        button_go[0].click()

        self.driver.switch_to.window(self.driver.window_handles[1])

        last_ninety_days_button = self.wait.until(ec.presence_of_element_located((By.XPATH, '//div[@class="ant-tabs-tab"][3]')))
        last_ninety_days_button.click()
        time.sleep(3)

        self.click_button(By.XPATH, "//label[@class='ant-radio-button-wrapper'][1]")
        self.click_button(By.XPATH, "//label[@class='ant-radio-button-wrapper'][2]")
        self.click_button(By.XPATH, "//label[@class='ant-radio-button-wrapper']")

        self.click_button(By.XPATH, '//div[@class="ant-tabs-tab"][2]')

        self.click_button(By.XPATH, "//label[@class='ant-radio-button-wrapper'][1]")
        self.click_button(By.XPATH, "//label[@class='ant-radio-button-wrapper'][2]")
        self.click_button(By.XPATH, "//label[@class='ant-radio-button-wrapper']")

        self.click_button(By.XPATH, '//div[@class="ant-tabs-tab"][2]')

        self.click_button(By.XPATH, "//label[@class='ant-radio-button-wrapper'][1]")
        self.click_button(By.XPATH, "//label[@class='ant-radio-button-wrapper'][2]")
        self.click_button(By.XPATH, "//label[@class='ant-radio-button-wrapper']")

        self.click_button(By.XPATH, '//div[@class="ant-tabs-tab"][1]')

        self.click_button(By.XPATH, "//label[@class='ant-radio-button-wrapper'][1]")
        self.click_button(By.XPATH, "//label[@class='ant-radio-button-wrapper'][2]")
        self.click_button(By.XPATH, "//label[@class='ant-radio-button-wrapper']")

# def run():
#     test_class = TestDays()
#     test_class.clean()
# run()
