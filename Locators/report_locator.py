from selenium.webdriver.common.by import By

class ReportLocator:
    CLOSE_WINDOW = (By.XPATH, "//span[@class='ant-modal-close-x']")
    REPORT_TITLE_NAME = (By.XPATH, "//*[contains(text(), 'Test')]")
    REPORT_SWITCH = (By.XPATH, "//li[@class='ant-list-item']")