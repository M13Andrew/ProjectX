from Pages.login import LoginPage
import time


class TestLogin:
    def test_login_validator(self, driver):
        login = LoginPage(driver, 'https://bes.datawiz.io/login/')
        login.open()
        login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
        time.sleep(5)

    def test_login_invalid_login(self, driver):
        login = LoginPage(driver, 'https://bes.datawiz.io/login/')
        login.open()
        login.login_valid('andrew.masyuk@datawiz.', 'Qweasd2zxc')
        error = login.get_error()
        assert  error == 'Будь ласка, введіть правильні e-mail та пароль. Зауважте, що поле "Пароль" чутливе до регістру.'
