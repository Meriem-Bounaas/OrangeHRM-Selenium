from faker import Faker
import random
import string

from selenium.webdriver.remote.webelement import WebElement
from selenium.common import StaleElementReferenceException
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

fake = Faker()

def wait_click(driver: WebDriver, element: WebElement) -> None:
    WebDriverWait(driver, 20, ignored_exceptions=[StaleElementReferenceException]).until(
        EC.element_to_be_clickable(element)).click()

def verify_header_of_my_info_page(element, text):
    return element.text == text

def generate_first_name():
    return fake.name().split(' ')[0]

def generate_last_name():
    return fake.name().split(' ')[1]

def generate_id():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(2))

def generate_password():
    return fake.password()

def generate_email():
    return fake.email()

def generate_city():
    return fake.city()

def generate_zip():
    return fake.postcode()
