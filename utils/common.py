from faker import Faker
import random
import string

fake = Faker()

# def find_element(driver, by_locator, locator):
#     return driver.find_element(by_locator, locator)

# def find_elements(driver, by_locator, locator):
#     return driver.find_elements(by_locator, locator)

def generate_first_name():
    return fake.name().split(' ')[0]

def generate_last_name():
    return fake.name().split(' ')[1]

def generate_id():
    characters = string.ascii_letters + string.digits 
    return ''.join(random.choice(characters) for _ in range(5))