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
        'loginbtn': ("XPATH", '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
    }

    def login(self, username: str, password: str) -> None:
        '''
        Function for logging using a username and password.
        '''
        self.driver.get(self.url)
        self.username.set_text(username)
        self.password.set_text(password)
        self.loginbtn.click_button()

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