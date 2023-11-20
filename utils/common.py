from faker import Faker
import random
import string

fake = Faker()


def verify_header_of_my_info_page(element, text):
    return element.text == text


def generate_first_name():
    return fake.name().split(' ')[0]


def generate_last_name():
    return fake.name().split(' ')[1]


def generate_id():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(5))


def generate_password():
    # return f'{random.randint(100, 500)}_{fake.first_name()}_{random.randint(600, 900)}'
    return fake.password()


def generate_email():
    return fake.email()


def generate_city():
    return fake.city()


def generate_zip():
    return fake.postcode()
