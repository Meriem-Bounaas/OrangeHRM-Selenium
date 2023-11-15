from selenium.webdriver.edge.webdriver import WebDriver
from src.base.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.title = 'OrangeHRM'
        self.url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
        self.header = ''

    locators = {
        'username': ("NAME", "username"),
        'password': ("NAME", "password"),
        'loginbtn': ("XPATH", '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
    }

    def login(self, username: str, password: str) -> None:
        self.driver.get(
            'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        self.username.set_text(username)
        self.password.set_text(password)
        self.loginbtn.click_button()

    def verify_page_title(self) -> bool:
        return self.driver.title == 'OrangeHRM'

    def verify_page_url(self) -> bool:
        return 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login' in self.driver.current_url

    def invalid_credentials():
        return 'Invalid credentials' in self.driver.page_source