from selenium.webdriver.edge.webdriver import WebDriver
from src.base.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.title = 'OrangeHRM'
        self.url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

    locators = {
        'username': ("NAME", "username"),
        'password': ("NAME", "password"),
        'login_button': ("XPATH", "//*[@id=\"app\"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"),
        'login_element': ("XPATH", "//*[text()='Login']")
    }

    def login(self, username: str, password: str) -> None:
        '''
        Function for logging using a username and password.
        '''
        self.driver.get(self.url)
        self.username.set_text(username)
        self.password.set_text(password)
        self.login_button.click_button()

    def verify_page_title(self) -> bool:
        '''
        Function to verify the title of the login page.
        '''
        return self.driver.title == self.title

    def verify_page_url(self) -> bool:
        '''
        Function to verify the URL of the login page.
        '''
        return self.url in self.driver.current_url

    def invalid_credentials(self) -> bool:
        '''
        Function to verify if an element with the text 'invalid credentials' appears.
        '''
        return 'Invalid credentials' in self.driver.page_source
    
    def verify_existence_of_login_text(self) -> bool:
        '''
        Function to verify the existence of the text 'Login' on the page.
        '''
        return bool(self.login_element)