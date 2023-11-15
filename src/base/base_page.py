from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage(PageFactory):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__()
        self.driver = driver

    locators = {
    }

    def verify_url(self, url: str) -> bool:
        return self.driver.current_url == url

    def verify_title(self, title: str) -> bool:
        return self.driver.title == title

    def verify_header(self, header_element: WebElement, header: str) -> bool:
        return header_element.text == header    
