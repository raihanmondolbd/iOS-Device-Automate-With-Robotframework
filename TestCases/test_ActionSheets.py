import time
from Pages.BasePage import BasePage
from Pages.ActionSheetsPage import ActionSheetPage
from Locators.Locators import iOSAppLocators

locator = iOSAppLocators


class LoginTest(BasePage):

    def test_iOSAutomate(self):
        a = ActionSheetPage(self.driver)
        time.sleep(2)
        a.click_action_sheets_button()
        time.sleep(2)
        a.click_ok_cancel_button()
        time.sleep(2)
        a.click_cancel()
        time.sleep(2)
        a.click_back_button()
        time.sleep(2)
        self.driver.swipe(152, 550, 152, 80, 1000)
        time.sleep(2)
        a.click_at(locator.text_fields)
        time.sleep(1)
        a.enter_text_at(locator.default_textbox, "dafault")
        time.sleep(1)
        a.enter_text_at(locator.tinted_textbox, "tinted")
        time.sleep(1)
        a.enter_text_at(locator.secured_textbox, "123456789")
        time.sleep(1)
        a.enter_text_at(locator.specific_keyboard_textbox, "specific keyboard")
        time.sleep(1)
        a.enter_text_at(locator.custom_textbox, "custom")
        time.sleep(1)
        a.click_at(locator.done_button)
        time.sleep(2)
        self.driver.back()
        time.sleep(1)
