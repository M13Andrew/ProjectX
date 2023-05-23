from Pages.login import LoginPage
from Pages.accountpage import AccountPage
import time


class TestDCAccount:


    def test_dc_account0(self, driver):
        login = LoginPage(driver, 'https://bes.datawiz.io/login/')
        login.open()
        login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
        account = AccountPage(driver)
        account.select_client(4, 0, 8)
        time.sleep(5)

    def test_dc_account1(self, driver):
        login = LoginPage(driver, 'https://bes.datawiz.io/login/')
        login.open()
        login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
        account = AccountPage(driver)
        account.select_client(4, 1, 8)
        time.sleep(5)

    def test_dc_account2(self, driver):
        login = LoginPage(driver, 'https://bes.datawiz.io/login/')
        login.open()
        login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
        account = AccountPage(driver)
        account.select_client(4, 2, 8)
        time.sleep(5)

    def test_dc_account3(self, driver):
        login = LoginPage(driver, 'https://bes.datawiz.io/login/')
        login.open()
        login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
        account = AccountPage(driver)
        account.select_client(4, 3, 8)
        time.sleep(5)

    def test_dc_account4(self, driver):
        login = LoginPage(driver, 'https://bes.datawiz.io/login/')
        login.open()
        login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
        account = AccountPage(driver)
        account.select_client(4, 4, 8)
        time.sleep(5)

    def test_dc_account5(self, driver):
        login = LoginPage(driver, 'https://bes.datawiz.io/login/')
        login.open()
        login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
        account = AccountPage(driver)
        account.select_client(4, 5, 8)
        time.sleep(5)

    def test_dc_account6(self, driver):
        login = LoginPage(driver, 'https://bes.datawiz.io/login/')
        login.open()
        login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
        account = AccountPage(driver)
        account.select_client(4, 6, 8)
        time.sleep(5)

    def test_dc_account7(self, driver):
        login = LoginPage(driver, 'https://bes.datawiz.io/login/')
        login.open()
        login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
        account = AccountPage(driver)
        account.select_client(4, 7, 8)
        time.sleep(5)

    def test_dc_account8(self, driver):
        login = LoginPage(driver, 'https://bes.datawiz.io/login/')
        login.open()
        login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
        account = AccountPage(driver)
        account.select_client(4, 8, 8)
        time.sleep(5)