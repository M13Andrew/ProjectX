from Pages.basepage import NextPage
from Locators.account_locators import AccountPageLocator
from selenium.webdriver.common.keys import Keys
import time

class AccountPage(NextPage):

    def select_client(self, dropdown_count, item_button, go_button):
        dropdown = self.elements_are_visible(AccountPageLocator.DROPDOWN)
        dropdown[dropdown_count].click()
        item = self.elements_are_visible(AccountPageLocator.ITEM_BUTTON)
        item[item_button].click()
        go = self.elements_are_visible(AccountPageLocator.GO_BUTTON)
        go[go_button].click()
        self.switch_to_another_window(1)

    def test_cicle(self, dropdown_count, go_button, count):
        item_button = 0
        client_position = 0
        count_position = count
        while client_position != count_position:
            if client_position < count_position:
                dropdown = self.elements_are_visible(AccountPageLocator.DROPDOWN)
                dropdown[dropdown_count].click()
                item = self.elements_are_visible(AccountPageLocator.ITEM_BUTTON)
                item[item_button].click()
                go = self.elements_are_visible(AccountPageLocator.GO_BUTTON)
                go[go_button].click()
                self.switch_to_another_window(1)
                time.sleep(1)
                self.element_is_visible(AccountPageLocator.FIND_ELEMENT).send_keys(Keys.CONTROL + 'w')
                self.close_window()
                self.switch_to_another_window(0)
                client_position +=1
                item_button += 1
            else:
                break

