from appium.webdriver.common.appiumby import AppiumBy


class iOSAppLocators:
    action_sheets = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Action Sheets"]')
    ok_cancel_button = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Okay / Cancel"]')
    cancel_popup = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Cancel"]')
    back = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="UICatalog"]')

    text_fields = (AppiumBy.ACCESSIBILITY_ID, 'Text Fields')
    default_textbox = (AppiumBy.XPATH, '//XCUIElementTypeTable[@type="XCUIElementTypeTable"]/XCUIElementTypeCell[1]')
    tinted_textbox = (AppiumBy.XPATH, '//XCUIElementTypeTable[@type="XCUIElementTypeTable"]/XCUIElementTypeCell[2]')
    secured_textbox = (AppiumBy.XPATH, '//XCUIElementTypeTable[@type="XCUIElementTypeTable"]/XCUIElementTypeCell[3]')
    specific_keyboard_textbox = (AppiumBy.XPATH, '//XCUIElementTypeTable[@type="XCUIElementTypeTable"]/XCUIElementTypeCell[4]')
    custom_textbox = (AppiumBy.XPATH, '//XCUIElementTypeTable[@type="XCUIElementTypeTable"]/XCUIElementTypeCell[5]')
    done_button = (AppiumBy.ACCESSIBILITY_ID, 'Done')
