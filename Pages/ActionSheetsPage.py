from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from Pages.homePage import HomePage
from Locators.Locators import iOSAppLocators


class ActionSheetPage(HomePage):

    def __init__(self, driver):
        self.locator = iOSAppLocators
        self.driver = driver
        super(ActionSheetPage, self).__init__(driver)

    def click_action_sheets_button(self):
        self.find_element(*self.locator.action_sheets).click()

    def click_ok_cancel_button(self):
        self.find_element(*self.locator.ok_cancel_button).click()

    def click_cancel(self):
        self.find_element(*self.locator.cancel_popup).click()

    def click_back_button(self):
        self.find_element(*self.locator.back).click()

    def enter_text_at(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    def click_at(self, locator):
        self.driver.find_element(*locator).click()

