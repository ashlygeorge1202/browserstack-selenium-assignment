from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OpinionPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def visit(self, url):
        self.driver.get(url)

    def wait_for(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))
