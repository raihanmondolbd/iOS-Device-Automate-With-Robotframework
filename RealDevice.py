import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

caps = {}
caps["platformName"] = "iOS"
caps["appium:platformVersion"] = "15.5"
caps["appium:deviceName"] = "iPhone 11"
caps["appium:app"] = "/Users/qups/Downloads/IOSAppium/IntegrationApp/IntegrationApp.app"
caps["appium:automationName"] = "XCUITest"
caps["appium:noReset"] = False
caps["appium:includeSafariInWebviews"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Action Sheets"]').click()
driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Okay / Cancel"]').click()
driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Cancel"]').click()
driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeButton[@name="UICatalog"]').click()

driver.swipe(152, 550, 152, 80, 1000)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Text Fields').click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeTable[@type="XCUIElementTypeTable"]/XCUIElementTypeCell[1]').send_keys("default")
time.sleep(1)
driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeTable[@type="XCUIElementTypeTable"]/XCUIElementTypeCell[2]').send_keys("tinted")
time.sleep(1)
driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeTable[@type="XCUIElementTypeTable"]/XCUIElementTypeCell[3]').send_keys("123456789")
time.sleep(1)
driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeTable[@type="XCUIElementTypeTable"]/XCUIElementTypeCell[4]').send_keys("specific keyboard")
time.sleep(1)
driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeTable[@type="XCUIElementTypeTable"]/XCUIElementTypeCell[5]').send_keys("custom")
time.sleep(2)
driver.back()

driver.quit()
