from src.base.base_page import BasePage
from selenium.webdriver.edge.webdriver import WebDriver

class DashboardPage(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.title = 'OrangeHRM'
        self.url = 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
        self.header = 'Dashboard'
    
    locators = {
        'header_element': ("XPATH", "//*[@id=\"app\"]/div[1]/div[1]/header/div[1]/div[1]/span/h6"),
        'PIM_button' : ("XPATH", "//*[@href=\"/web/index.php/pim/viewPimModule\"]"),
        'user_button' : ("XPATH", "//*[@class= 'oxd-userdropdown-tab']"),
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
        self.PIM_button.click_button()

    def logout(self) -> None:
        '''
        Function to Logout.
        '''
        self.user_button.click_button()
        self.logout_button.click_button()


