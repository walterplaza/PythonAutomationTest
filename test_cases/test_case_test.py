from test_cases.test_base import TestBase as TB
from utilities.webdriver_wrapper import WebDriverWrapper as SW
from page_objects.google_page import GooglePage as GP



def first_test():
    test_base = TB()
    google_page = GP()
    google_page = google_page.create_instance()


    google_page.search("kamikasi")
    SW.close()


first_test()

