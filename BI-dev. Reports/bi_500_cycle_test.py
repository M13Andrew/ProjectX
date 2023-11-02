from Pages.login import LoginPage
from Pages.accountpage import MainPageDelete


class TestReports:

    def test_new_cycle(self, driver):
        login = LoginPage(driver, "https://bi-dev.datawiz.io/c/277/home")
        login.open()
        login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
        cycle = MainPageDelete(driver)
        cycle.
