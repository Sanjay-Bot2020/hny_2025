from selenium.webdriver.common.by import By

class functions():
    def __init__(self, driver):
        self.driver = driver

    def get_Type(self, loctype):

        self.loctype = loctype.lower()
        if self.loctype == "xpath":
            return By.XPATH
        elif self.loctype == "id":
            return By.ID
        elif self.loctype == "css":
            return By.CSS_SELECTOR
        else:
            print("Incorrect By Type")
            return False


    def find_element(self, loctype, loc):
        self.loctype = self.get_Type(loctype)
        element = self.driver.find_element(self.loctype, loc)
        return element

    def is_element_displayed(self, loctype, loc):
        element = self.find_element(loctype, loc)
        if element.is_displayed():
            return True
        else:
            return False

    # def explicit_wait(self, timeout, pollfrq, loctype, loc):





