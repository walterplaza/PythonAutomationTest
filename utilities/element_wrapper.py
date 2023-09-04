from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.webdriver_wrapper import WebDriverWrapper as SW


class ElementWrapper:
    def __init__(self, locator):
        self.locator = locator
        self.element = None

    def find(self):
        if self.element is None:
            self.element = WebDriverWait(SW.get_driver_instance(), 10).until(EC.presence_of_element_located(self.locator))
        return self.element

    def send_keys(self, text):
        self.find().send_keys(text)
