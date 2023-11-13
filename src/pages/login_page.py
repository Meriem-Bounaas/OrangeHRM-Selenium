from selenium.webdriver.common.by import By
from utils.common import find_element
from seleniumpagefactory.Pagefactory import PageFactory


class LoginPage(PageFactory):
    def __init__(self, driver) -> None:
        self.driver = driver

    locators = {
        'username': ("NAME", "username"),
        'password': ("NAME", "password"),
        'loginbtn': ("XPATH", '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
    }

    def login(self, email: str, psw: str) -> None:
        self.driver.get(
            'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        self.username.set_text(email)
        self.password.set_text(psw)
        self.loginbtn.click_button()

    def verify_page_title(self) -> bool:
        return self.driver.title == 'OrangeHRM'

    def verify_page_url(self) -> bool:
        return 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login' in self.driver.current_url
