from imports import *

class TestOne:

    def test_one(self):
        driver_service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        options.add_argument("--incognito")
        driver = webdriver.Chrome(service=driver_service, options=options)
        #driver = webdriver.Chrome(service=driver_service)
        driver.maximize_window()
        driver.get('https://demoqa.com/buttons')
        wait = WebDriverWait(driver, 15, 0.3)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-primary']")))
        button = driver.find_elements(By.XPATH, "//button[@class='btn btn-primary']")
        button[2].click()
        wait.until(ec.visibility_of_element_located((By.ID, 'dynamicClickMessage')))
        message = driver.find_element(By.ID, 'dynamicClickMessage')
        assert message.text == 'You have done a dynamic click'
        time.sleep(1)
        driver.quit()