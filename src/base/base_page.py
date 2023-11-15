from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage(PageFactory):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__()
        self.driver = driver

    def verify_url(self, url: str) -> bool:
        '''
        Function to verify the URL.
        '''
        return self.driver.current_url == url

    def verify_title(self, title: str) -> bool:
        '''
        Function to verify the title.
        '''
        return self.driver.title == title

    def verify_header(self, header_element: WebElement, header: str) -> bool:
        '''
        Function to verify the header.
        '''
        return header_element.text == header    