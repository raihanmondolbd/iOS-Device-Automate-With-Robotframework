*** Settings ***
Library  AppiumLibrary
Library  BuiltIn


*** Variables ***
${ANDROID_AUTOMATION_NAME}    UIAutomator2
${ANDROID_APP}                ${CURDIR}/../demoapp/ApiDemos-debug.apk
${ANDROID_PLATFORM_NAME}      Android
${ANDROID_PLATFORM_VERSION}   %{ANDROID_PLATFORM_VERSION=11}
${ANDROID_APP_PACKAGE}        io.appium.android.apis

${IOS_AUTOMATION_NAME}        XCUITest
#${IOS_APP}                    ${CURDIR}/../demoapp/TestApp.app.zip
${IOS_APP}                    ${CURDIR}/../APP/UICatalog.app
${IOS_PLATFORM_NAME}          iOS
${IOS_PLATFORM_VERSION}       %{IOS_PLATFORM_VERSION=15.5}
${IOS_DEVICE_NAME}            iPhone 8 Plus
${NO_RESET}                   False

*** Test Cases ***
OPEN_APP
    Open iOS Test App



*** Keywords ***
Open Android Test App
  [Arguments]    ${appActivity}=${EMPTY}
  open application  http://127.0.0.1:4723/wd/hub  automationName=${ANDROID_AUTOMATION_NAME}
  ...  app=${ANDROID_APP}  platformName=${ANDROID_PLATFORM_NAME}  platformVersion=${ANDROID_PLATFORM_VERSION}
  ...  appPackage=${ANDROID_APP_PACKAGE}  appActivity=${appActivity}


Open iOS Test App
  open application  http://127.0.0.1:4723/wd/hub  automationName=${IOS_AUTOMATION_NAME}
  ...  app=${IOS_APP}  platformName=${IOS_PLATFORM_NAME}  platformVersion=${IOS_PLATFORM_VERSION}
  ...  deviceName=${IOS_DEVICE_NAME}  noReset=${NO_RESET}

  click element  //XCUIElementTypeStaticText[@name="Action Sheets"]
  Sleep  1
  click element  //XCUIElementTypeStaticText[@name="Okay / Cancel"]
  sleep  1
  click element  //XCUIElementTypeButton[@name="Cancel"]
  Sleep  1
  click element  //XCUIElementTypeButton[@name="UICatalog"]
  Sleep  1
  scroll down  Text Fields
  sleep  1
  click element  Text Fields
  input text  //XCUIElementTypeTable[@type="XCUIElementTypeTable"]/XCUIElementTypeCell[1]  default
  sleep  1
  input text  //XCUIElementTypeTable[@type="XCUIElementTypeTable"]/XCUIElementTypeCell[2]  tinted
  sleep  1
  input text  //XCUIElementTypeTable[@type="XCUIElementTypeTable"]/XCUIElementTypeCell[3]  123456789
  sleep  1
  input text  //XCUIElementTypeTable[@type="XCUIElementTypeTable"]/XCUIElementTypeCell[4]  specefic keyboard
  sleep  1
  input text  //XCUIElementTypeTable[@type="XCUIElementTypeTable"]/XCUIElementTypeCell[5]  custom
  sleep  1
  click element  //XCUIElementTypeButton[@name="Done"]
  go back
  quit application