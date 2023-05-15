from Pages.login import LoginPage
from Pages.accountpage import AccountPage
import time


class TestAccountInfo:
    def test_account_info(self, driver):
        login = LoginPage(driver, 'https://bes.datawiz.io/login/')
        login.open()
        login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
        account = AccountPage(driver)
        account.select_client(0, 1, 0)
        time.sleep(5)