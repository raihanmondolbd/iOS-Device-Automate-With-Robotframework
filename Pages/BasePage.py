from appium import webdriver
import unittest


class BasePage(unittest.TestCase):

    def setUp(self):
        caps = {}
        caps["platformName"] = "iOS"
        caps["appium:platformVersion"] = "15.5"
        caps["appium:deviceName"] = "iPhone 8 Plus"
        caps["appium:app"] = "/Users/qups/Downloads/IOSAppium/APP/UICatalog.app"
        caps["appium:automationName"] = "XCUITest"
        caps["appium:noReset"] = False
        caps["appium:includeSafariInWebviews"] = True
        caps["appium:newCommandTimeout"] = 3600
        caps["appium:connectHardwareKeyboard"] = True

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

        print("Test Started.......")

    def tearDown(self):
        self.driver.quit()
        print("Test Completed")




if __name__ == "__main__":
    unittest.main()

