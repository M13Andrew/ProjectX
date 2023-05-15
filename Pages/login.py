from Pages.basepage import BasePage
from Locators.login_locator import LoginPageLocators


class LoginPage(BasePage):

    def login_valid(self, login, password):
        self.element_is_visible(LoginPageLocators.LOGIN_INPUT).send_keys(login)
        self.element_is_visible(LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.element_is_visible(LoginPageLocators.LOGIN_BUTTON).click()

    def get_error(self):
        error = self.element_is_visible(LoginPageLocators.LOGIN_ERROR).text
        return error