


class HomePage:
    def __init__(self, driver, base_url=""):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 30

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def go_back(self):
        self.driver.back()

    # def enter_text_at(self, locator, value):
    #     self.driver.find_element(*locator).send_keys(value)



