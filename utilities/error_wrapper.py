from utilities.webdriver_wrapper import WebDriverWrapper


class ErrorWrapper(Exception):
    def __init__(self, opt_error=None):
        super().__init__(opt_error)


class CustomErrorWrapper(ErrorWrapper):
    @staticmethod
    def get_function_name(func_name):
        return func_name.__name__

    def __init__(self, function_name, error_message):
        super().__init__(error_message)
        WebDriverWrapper.take_screenshot("test_screenshot")
        self.message = f"{error_message} -> Action '{CustomErrorWrapper.get_function_name(function_name)}'"
        raise Exception(self.message)


class ElementNotSelectTableErrorWrapper(ErrorWrapper):
    def __init__(self, by):
        super().__init__()
        self.message = f"ElementNotSelectTableError - The element {by} could not be selected."

