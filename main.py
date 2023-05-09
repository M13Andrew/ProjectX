from selenium import webdriver
from selenium.webdriver import Keys
import time
from selenium.webdriver.chrome.options import Options #as chrome_options
#from fake_useragent import UserAgent
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
driver.maximize_window()
wait = WebDriverWait(browser, 15, 0.3)
