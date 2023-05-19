from Pages.login import LoginPage
from Pages.accountpage import AccountPage


class TestBiCycle:

    def test_new_cycle(self, driver):
        login = LoginPage(driver, "https://bes.datawiz.io/login/")
        login.open()
        login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
        cycle = AccountPage(driver)
        cycle.test_cycle(0, 0, 11)







    # example (for)
    # def bi_account(self, driver, client_position):
    #     login = LoginPage(driver, "https://bes.datawiz.io/login/")
    #     login.open()
    #     login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
    #     account = AccountPage(driver)
    #     account.select_client(0, client_position, 0)
    #     time.sleep(5)
    # def test_cycle(self, driver):
    #     for client_position in [0, 1, 2, 3, 4]:
    #         self.test_bi_account(driver, client_position)