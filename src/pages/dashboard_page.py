from selenium.webdriver.common.by import By
from utils.common import find_element


class DashboardPage:

    def __init__(self, driver) -> None:
        self.driver = driver

    def verify_page_title(self) -> bool:
        return self.driver.title == 'OrangeHRM'

    def verify_page_url(self) -> bool:
        return 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index' in self.driver.current_url