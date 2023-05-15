from Pages.basepage import NextPage
from Locators.account_locators import AccountPageLocator


class AccountPage(NextPage):

    def select_client(self, dropdown_count, item_button, go_button):
        dropdown = self.elements_are_visible(AccountPageLocator.DROPDOWN)
        dropdown[dropdown_count].click()
        item = self.elements_are_visible(AccountPageLocator.ITEM_BUTTON)
        item[item_button].click()
        go = self.elements_are_visible(AccountPageLocator.GO_BUTTON)
        go[go_button].click()
        self.switch_to_another_window(1)