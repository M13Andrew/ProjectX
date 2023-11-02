from Pages.basepage import NextPage
from Locators.report_locator import ReportLocator
from selenium.webdriver.common.keys import Keys
import time

class MainPageDelete(NextPage):

    def close_modal_window(self):
        self.element_is_visible(ReportLocator.CLOSE_WINDOW).click()
        self.element_is_visible(ReportLocator.REPORT_TITLE_NAME).click()

    def report_cycle(self):
        report_counters = self.elements_are_visible(ReportLocator.REPORT_SWITCH)
        amount_of_counters = len(report_counters)
        item = 0
        while item != amount_of_counters:
            counters = report_counters
            counters[item].click()
            time.sleep(1)
            item += 1


