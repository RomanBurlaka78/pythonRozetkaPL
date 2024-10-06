from conftest import driver


class BasePage:
    URL = "https://rozetka.pl/"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def show_title(self):
        return self.driver.title

    def show_url(self):
        return self.driver.current_url

