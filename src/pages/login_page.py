from selenium.webdriver.common.by import By
from utils.common import find_element


class LoginPage:
    def __init__(self, driver) -> None:
        self.driver = driver

    locators = {
        'username': ("NAME", "username"),
        'password': ("NAME ", "password"),
        'loginbtn': ("TAG_NAME ", "button")
    }

    def login(self, email: str, psw: str) -> None:
        self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        self.username.set_text(email)
        self.password.set_text(psw)
        self.loginbtn.click_button()
        # username = self.driver.find_element(By.NAME, 'username')
        # username.send_keys(email)
        # password = self.driver.find_element(By.NAME, 'password')
        # password.send_keys(email)
        # loginbtn = self.driver.find_element(By.TAG_NAME, 'button')
        # loginbtn.click()


    def verify_page_title(self) -> bool:
        return self.driver.title == 'OrangeHRM'

    def verify_page_url(self) -> bool:
        return 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login' in self.driver.current_url