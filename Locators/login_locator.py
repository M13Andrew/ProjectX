from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_INPUT = (By.ID, 'id_auth-username')
    PASSWORD_INPUT = (By.ID, 'id_auth-password')
    LOGIN_BUTTON = (By.XPATH, "//button[@class='btn btn-primary btn-block']")
    LOGIN_ERROR = (By.XPATH, "//ul[@class='errorlist nonfield']")