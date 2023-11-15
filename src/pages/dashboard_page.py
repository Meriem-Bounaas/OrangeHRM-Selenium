from src.base.base_page import BasePage
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

class DashboardPage(BasePage):

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.title = 'OrangeHRM'
        self.url = 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
        self.header = 'Dashboard'
    
    locators = {
        'header_element': ("XPATH", "//*[@id=\"app\"]/div[1]/div[1]/header/div[1]/div[1]/span/h6"),
    }

    def verify_page(self) -> bool:
        return super().verify_url(self.url) and super().verify_title(self.title) and super().verify_header(self.header_element, self.header)
