from Pages.login import LoginPage
from Pages.accountpage import AccountPage
import time


class TestBiAccountInfo:

    def bi_account(self, driver, client_position):
        login = LoginPage(driver, "https://bes.datawiz.io/login/")
        login.open()
        login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
        account = AccountPage(driver)
        account.select_client(0, client_position, 0)
        time.sleep(5)


    # def test_cycle(self, driver):
    #     for client_position in [0, 1, 2, 3, 4]:
    #         self.test_bi_account(driver, client_position)


    def test_new_cycle(self, driver):
        login = LoginPage(driver, "https://bes.datawiz.io/login/")
        login.open()
        login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
        cycle = AccountPage(driver)
        cycle.test_cicle(0, 0, 10)

    # def test_bi_account_info1(self, driver):
    #     login = LoginPage(driver, 'https://bes.datawiz.io/login/')
    #     login.open()
    #     login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
    #     account = AccountPage(driver)
    #     account.select_client(0, 1, 0)
    #     time.sleep(5)


    # def test_account_info2(self, driver):
    #     login = LoginPage(driver, 'https://bes.datawiz.io/login/')
    #     login.open()
    #     login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
    #     account = AccountPage(driver)
    #     account.select_client(0, 0, 0)
    #     time.sleep(5)
    #
    #
    # def test_account_info3(self, driver):
    #     login = LoginPage(driver, 'https://bes.datawiz.io/login/')
    #     login.open()
    #     login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
    #     account = AccountPage(driver)
    #     account.select_client(0, 2, 0)
    #     time.sleep(5)
    #
    #
    # def test_account_info4(self, driver):
    #     login = LoginPage(driver, 'https://bes.datawiz.io/login/')
    #     login.open()
    #     login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
    #     account = AccountPage(driver)
    #     account.select_client(0, 3, 0)
    #     time.sleep(5)
    #
    #
    # def test_account_info5(self, driver):
    #     login = LoginPage(driver, 'https://bes.datawiz.io/login/')
    #     login.open()
    #     login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
    #     account = AccountPage(driver)
    #     account.select_client(0, 4, 0)
    #     time.sleep(5)
    #
    #
    # def test_account_info6(self, driver):
    #     login = LoginPage(driver, 'https://bes.datawiz.io/login/')
    #     login.open()
    #     login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
    #     account = AccountPage(driver)
    #     account.select_client(0, 5, 0)
    #     time.sleep(5)
    #
    #
    # def test_account_info7(self, driver):
    #     login = LoginPage(driver, 'https://bes.datawiz.io/login/')
    #     login.open()
    #     login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
    #     account = AccountPage(driver)
    #     account.select_client(0, 6, 0)
    #     time.sleep(5)
    #
    #
    # def test_account_info8(self, driver):
    #     login = LoginPage(driver, 'https://bes.datawiz.io/login/')
    #     login.open()
    #     login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
    #     account = AccountPage(driver)
    #     account.select_client(0, 7, 0)
    #     time.sleep(5)
    #
    #
    # def test_account_info9(self, driver):
    #     login = LoginPage(driver, 'https://bes.datawiz.io/login/')
    #     login.open()
    #     login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
    #     account = AccountPage(driver)
    #     account.select_client(0, 8, 0)
    #     time.sleep(5)
    #
    #
    # def test_account_info10(self, driver):
    #     login = LoginPage(driver, 'https://bes.datawiz.io/login/')
    #     login.open()
    #     login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
    #     account = AccountPage(driver)
    #     account.select_client(0, 9, 0)
    #     time.sleep(5)


    def test_cicle(self, driver):
        for client_position in [0, 1, 2, 3, 4]:
            self.test_bi_account(driver, client_position)

