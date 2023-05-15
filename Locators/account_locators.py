from selenium.webdriver.common.by import By


class AccountPageLocator:
    DROPDOWN = (By.XPATH, "//div[@class='ant-select-selector']")
    ITEM_BUTTON = (By.XPATH, "//div[@class='ant-select-item-option-content']")
    GO_BUTTON = (By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-block dw-btn']")

class PrivetCabinetLocator:
