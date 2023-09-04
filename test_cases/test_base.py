from utilities.webdriver_wrapper import WebDriverWrapper as SW


class TestBase:
    def __init__(self):
        self.navigate_to_web_page("https://www.google.com")

    @staticmethod
    def navigate_to_web_page(url):
        # SeleniumWrapper.restart()
        SW.open_url(url)
