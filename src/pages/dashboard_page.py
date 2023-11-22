from selenium.webdriver.edge.webdriver import WebDriver

from src.base.base_page import BasePage
from utils.common import *

class DashboardPage(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.title = 'OrangeHRM'
        self.url = 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
        self.header = 'Dashboard'
    
    locators = {
        'header_element': ("XPATH", "//span[@class= 'oxd-topbar-header-breadcrumb']/descendant::h6"),
        'pim_button' : ("XPATH", "//*[@href=\"/web/index.php/pim/viewPimModule\"]"),
        'user_button' : ("XPATH", "//span[@class= 'oxd-userdropdown-tab']"),
        'logout_button' : ("XPATH", "//*[@href='/web/index.php/auth/logout']")
    }

    def verify_page(self) -> bool:
        '''
        Function to verify url and title and header of the dashboard login.
        '''
        return super().verify_url(self.url) and super().verify_title(self.title) and super().verify_header(self.header_element, self.header)
    
    def go_to_pim_page(self) -> None:
        '''
        Function to go to PIM Page.
        '''
        wait_click(self.driver, self.pim_button)

    def logout(self) -> None:
        '''
        Function to Logout.
        '''
        wait_click(self.driver, self.user_button)
        wait_click(self.driver, self.logout_button)