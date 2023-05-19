from Pages.login import LoginPage
from Pages.accountpage import AccountPage


class TestBiCycle:

    def test_new_cycle(self, driver):
        login = LoginPage(driver, "https://bes.datawiz.io/login/")
        login.open()
        login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
        cycle = AccountPage(driver)
        cycle.test_cycle(0, 0, 10)

    # example (for)
    # def test_cycle(self, driver):
    #     for client_position in [0, 1, 2, 3, 4]:
    #         self.test_bi_account(driver, client_position)
