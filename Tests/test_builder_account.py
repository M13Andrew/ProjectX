from Pages.login import LoginPage
from Pages.accountpage import AccountPage
import time


class TestBuilderAccount:


    def test_builder_account0(self, driver):
        login = LoginPage(driver, 'https://bes.datawiz.io/login/')
        login.open()
        login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
        account = AccountPage(driver)
        account.select_client(1, 0, 1)
        time.sleep(5)

    def test_builder_account1(self, driver):
        login = LoginPage(driver, 'https://bes.datawiz.io/login/')
        login.open()
        login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
        account = AccountPage(driver)
        account.select_client(1, 1, 1)
        time.sleep(5)

    def test_builder_account2(self, driver):
        login = LoginPage(driver, 'https://bes.datawiz.io/login/')
        login.open()
        login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
        account = AccountPage(driver)
        account.select_client(1, 2, 1)
        time.sleep(5)

    def test_builder_account3(self, driver):
        login = LoginPage(driver, 'https://bes.datawiz.io/login/')
        login.open()
        login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
        account = AccountPage(driver)
        account.select_client(1, 3, 1)
        time.sleep(5)

    def test_builder_account4(self, driver):
        login = LoginPage(driver, 'https://bes.datawiz.io/login/')
        login.open()
        login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
        account = AccountPage(driver)
        account.select_client(1, 4, 1)
        time.sleep(5)

    def test_builder_account5(self, driver):
        login = LoginPage(driver, 'https://bes.datawiz.io/login/')
        login.open()
        login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
        account = AccountPage(driver)
        account.select_client(1, 5, 1)
        time.sleep(5)

    def test_builder_account6(self, driver):
        login = LoginPage(driver, 'https://bes.datawiz.io/login/')
        login.open()
        login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
        account = AccountPage(driver)
        account.select_client(1, 6, 1)
        time.sleep(5)

    def test_builder_account7(self, driver):
        login = LoginPage(driver, 'https://bes.datawiz.io/login/')
        login.open()
        login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
        account = AccountPage(driver)
        account.select_client(1, 7, 1)
        time.sleep(5)

    def test_builder_account8(self, driver):
        login = LoginPage(driver, 'https://bes.datawiz.io/login/')
        login.open()
        login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
        account = AccountPage(driver)
        account.select_client(1, 8, 1)
        time.sleep(5)

    def test_builder_account9(self, driver):
        login = LoginPage(driver, 'https://bes.datawiz.io/login/')
        login.open()
        login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
        account = AccountPage(driver)
        account.select_client(1, 9, 1)
        time.sleep(5)
