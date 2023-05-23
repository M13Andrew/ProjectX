from Pages.login import LoginPage
from Pages.accountpage import AccountPage


class TestDCCycle:

    def test_dc_cycle(self, driver):
        login = LoginPage(driver, "https://bes.datawiz.io/login/")
        login.open()
        login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
        cycle = AccountPage(driver)
        cycle.test_cycle(3, 8, 9)