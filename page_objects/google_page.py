from utilities.error_wrapper import CustomErrorWrapper
from utilities.element_wrapper import ElementWrapper as EW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utilities.logger import Logger


class GooglePage:
    txt_search_box = EW((By.XPATH, "//textarea[@name='qs']"))

    @classmethod
    def create_instance(cls):
        instance = cls()
        return instance

    def search(self, value):
        try:
            Logger.info("sending text to the page search field.")
            self.txt_search_box.send_keys(value)
        except Exception as e:
            raise CustomErrorWrapper(self.search, e)
