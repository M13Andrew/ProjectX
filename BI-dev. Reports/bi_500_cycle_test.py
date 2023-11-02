from Pages.login import LoginPage
from Pages.main_page_delete import MainPageDelete
import time


class TestReports:

    def test_new_cycle(self, driver):
        login = LoginPage(driver, "https://bi-dev.datawiz.io/c/277/home")
        login.open()
        login.login_valid('andrew.masyuk@datawiz.io', 'Qweasd2zxc')
        main_page = MainPageDelete(driver)
        main_page.close_modal_window()
        main_page.report_cycle()
        time.sleep(5)
