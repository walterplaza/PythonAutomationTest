import base64

from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebDriverWrapper:
    current_browser = None
    browser_array = []

    # def __init__(self, browser="chrome", driver_path=None):
    #     if browser == "chrome":
    #         self.driver = webdriver.Chrome()

    @staticmethod
    def get_driver_instance():
        try:
            if len(WebDriverWrapper.browser_array) == 0:
                WebDriverWrapper.current_browser = webdriver.Chrome()
                WebDriverWrapper.browser_array.append(WebDriverWrapper.current_browser)
                return WebDriverWrapper.current_browser
            else:
                return WebDriverWrapper.current_browser
        except Exception as e:
            print("An error occurred:", e)

    @staticmethod
    def open_url(url):
        try:
            current_browser = WebDriverWrapper.get_driver_instance()
            current_browser.get(url)
        except Exception as e:
            print("An error occurred:", e)

    @staticmethod
    def close():
        try:
            WebDriverWrapper.get_driver_instance().quit()
        except Exception as e:
            print("An error occurred:", e)

    @staticmethod
    def take_screenshot(name_of_pic):
        local_path = 'C:/practice projects/PythonSelenium1/conf/screen'

        try:
            screenshot_path = os.path.join(local_path, f"{name_of_pic}.png")
            driver = WebDriverWrapper.get_driver_instance()
            png = driver.get_screenshot_as_base64()
            decoded_data = base64.b64decode(png)

            if png is None or png == "":
                png = ""

            with open(screenshot_path, 'wb') as stream:
                stream.write(decoded_data)

        except Exception as err:
            print(f"Error when taking a screenshot with error: {err}")
