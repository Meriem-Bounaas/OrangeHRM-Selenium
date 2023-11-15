from faker import Faker
import random
import string

fake = Faker()

def generate_first_name():
    return fake.name().split(' ')[0]

def generate_last_name():
    return fake.name().split(' ')[1]

def generate_id():
    characters = string.ascii_letters + string.digits 
    return ''.join(random.choice(characters) for _ in range(5))