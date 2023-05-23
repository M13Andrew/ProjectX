from Pages.login import LoginPage
from Pages.accountpage import AccountPage
import time


class TestAPAccount:


    def test_ap_account0(self, driver):
        login = LoginPage(driver, 'https://bes.datawiz.io/login/')
        login.open()
        login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
        account = AccountPage(driver)
        account.select_client(3, 0, 7)
        time.sleep(5)

    def test_ap_account1(self, driver):
        login = LoginPage(driver, 'https://bes.datawiz.io/login/')
        login.open()
        login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
        account = AccountPage(driver)
        account.select_client(3, 1, 7)
        time.sleep(5)

    def test_ap_account2(self, driver):
        login = LoginPage(driver, 'https://bes.datawiz.io/login/')
        login.open()
        login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
        account = AccountPage(driver)
        account.select_client(3, 2, 7)
        time.sleep(5)

    def test_ap_account3(self, driver):
        login = LoginPage(driver, 'https://bes.datawiz.io/login/')
        login.open()
        login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
        account = AccountPage(driver)
        account.select_client(3, 3, 7)
        time.sleep(5)

    def test_ap_account4(self, driver):
        login = LoginPage(driver, 'https://bes.datawiz.io/login/')
        login.open()
        login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
        account = AccountPage(driver)
        account.select_client(3, 4, 7)
        time.sleep(5)

    def test_ap_account5(self, driver):
        login = LoginPage(driver, 'https://bes.datawiz.io/login/')
        login.open()
        login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
        account = AccountPage(driver)
        account.select_client(3, 5, 7)
        time.sleep(5)

    def test_ap_account6(self, driver):
        login = LoginPage(driver, 'https://bes.datawiz.io/login/')
        login.open()
        login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
        account = AccountPage(driver)
        account.select_client(3, 6, 7)
        time.sleep(5)

    def test_ap_account7(self, driver):
        login = LoginPage(driver, 'https://bes.datawiz.io/login/')
        login.open()
        login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
        account = AccountPage(driver)
        account.select_client(3, 7, 7)
        time.sleep(5)

    def test_ap_account8(self, driver):
        login = LoginPage(driver, 'https://bes.datawiz.io/login/')
        login.open()
        login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
        account = AccountPage(driver)
        account.select_client(3, 8, 7)
        time.sleep(5)

