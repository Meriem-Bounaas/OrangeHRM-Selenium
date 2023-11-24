from pathlib import Path
import pandas as pd
import csv
import os
import time

from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By

from src.base.base_page import BasePage
from utils.common import *


class PimPage(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.title = 'OrangeHRM'
        self.url = 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList'
        self.header = 'PIM'

    locators = {
        'required_text': ("XPATH", "//*[text()='Required']"),
        'search_button': ("XPATH", "//*[@type='submit']"),
        'reset_button': ("XPATH", "//*[@type='reset']"),
        'pencil_button': ("XPATH", "//*[@class='oxd-icon bi-pencil-fill']"),
        'first_name_input': ("XPATH", "//*[@name='firstName']"),
        'last_name_input': ("XPATH", "//*[@name='lastName']"),
        'header_element': ("XPATH", "//span[@class='oxd-topbar-header-breadcrumb']/h6"),
        'add_button': ("XPATH", "//div[@class='orangehrm-header-container']/button"),
        'id_employee_input': ("XPATH", "//label[text() = 'Employee Id']/parent::div/following-sibling::div/input"),
        'save_button': ("XPATH", "//*[@type='submit']"),
        'create_login_detail_button': ("XPATH", "//*[@class='oxd-switch-input oxd-switch-input--active --label-right']"),
        'profile_picture_element': ("XPATH", "//*[@class='employee-image']"),
        'username_input': ("XPATH", "//label[text() = 'Username']/parent::div/following-sibling::div/input"),
        'password_input': ("XPATH", "//label[text() = 'Password']/parent::div/following-sibling::div/input"),
        'confirm_password_input': ("XPATH", "//label[text() = 'Confirm Password']/parent::div/following-sibling::div/input")
    }

    def verify_page(self) -> bool:
        '''
        Function to verify url and title and header of the dashboard login.
        '''
        return super().verify_url(self.url) and super().verify_title(self.title) and super().verify_header(self.header_element, self.header)

    def verify_existence_of_add_employee_text(self) -> bool:
        '''
        Function to verify the existence of the text 'add employee' on the page.
        '''
        return bool(self.save_button)

    def verify_existence_of_profile_picture(self) -> bool:
        '''
        Function to verify the existence of the text 'Personel Details' on the page.
        '''
        return bool(self.profile_picture_element)

    def verify_existence_of_required_text(self) -> bool:
        '''
        Function to verify the existence of the text 'Required' on the page.
        '''
        return bool(self.required_text)

    def click_button_add_employee(self) -> None:
        '''
        Function to click the 'Add' button for adding an employee.
        '''
        wait_click(self.driver, self.add_button)

    def save_data_csv(self, file_name, header_row, data_row):
        '''
        Function to save data in csv file.
        '''
        path = Path(__file__).parent.parent.parent

        filename = os.path.join(
            path, f'test/assets/{file_name}')
        file_exists = os.path.isfile(filename)

        with open(filename, 'a', encoding="UTF8", newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(header_row)
            writer.writerow(data_row)

    def fill_form_employee(self, with_username) -> None:
        '''
        Function to populate the employee form.
        '''
        first_name = generate_first_name()
        last_name = generate_last_name()
        id_employee = generate_id()
        password = generate_password()
        user_name = first_name+last_name

        if with_username:
            self.first_name_input.set_text(first_name)
            self.last_name_input.set_text(last_name)
            self.id_employee_input.set_text(id_employee)

            new_id_employee = self.id_employee_input.get_attribute('value')

            wait_click(self.driver, self.create_login_detail_button)

            self.username_input.set_text(user_name)
            self.password_input.set_text(password)
            self.confirm_password_input.set_text(password)

            wait_click(self.driver, self.save_button)

            self.save_data_csv('data_login_employees_valid.csv', [
                               'username', 'password'], [user_name, password])
            self.save_data_csv('data_employees_informations.csv', ['id_employee', 'first_name', 'last_name', 'username', 'password'], [
                               new_id_employee, first_name, last_name, user_name, password])

        else:
            self.id_employee_input.set_text(generate_id())
            wait_click(self.driver, self.save_button)

        time.sleep(1)

    def search_employee_by_id(self) -> object:
        '''
        Function to search an employee using ID.
        '''
        path = Path(__file__).parent.parent.parent
        filename = os.path.join(
            path, 'test/assets/data_employees_informations.csv')
        
        with open(filename, encoding="UTF8", newline='') as f:
            heading = next(f)
            reader = csv.reader(f)
            chosen_row = random.choice(list(reader))

        id_employee = chosen_row[0]
        first_name = chosen_row[1]
        last_name = chosen_row[2]

        wait_click(self.driver, self.reset_button)
        self.id_employee_input.set_text(id_employee)
        wait_click(self.driver, self.search_button)

        return ([id_employee, first_name, last_name])

    def verify_existence_of_one_employee(self, employee_details) -> bool:
        '''
        Function to verify the existence of one employee in the employees table with the correct username and ID.
        '''
        employees_table = self.driver.find_elements(
            By.XPATH, "//*[@class='oxd-table-card']")

        id_employee = employees_table[0].text.splitlines()[0]
        first_name = employees_table[0].text.splitlines()[1]
        last_name = employees_table[0].text.splitlines()[2]

        return (len(employees_table) == 1) and (id_employee == employee_details[0]) and (first_name == employee_details[1]) and (last_name == employee_details[2])
    
    def update_csv_employee_id(self, old_id, new_id):
        '''
        Function to update employee id in csv file.
        '''
        path = Path(__file__).parent.parent.parent
        filename = os.path.join(
            path, 'test/assets/data_employees_informations.csv')

        employee_informations_row = []
        data = pd.read_csv(filename)

        for i, row in enumerate(data.itertuples()):
            id_employee = row.id_employee
            first_name = row.first_name
            last_name = row.last_name
            username = row.username
            password = row.password

            if id_employee == old_id:
                employee_informations_row.append(row)

                df = data.drop(data.index[i])
                df.to_csv(filename, index=False)
                break
        
        employee_informations_row[0] = new_id
        employee_informations_row.append(first_name)
        employee_informations_row.append(last_name)
        employee_informations_row.append(username)
        employee_informations_row.append(password)

        with open(filename, 'a', encoding="UTF8", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(employee_informations_row)

    def update_id_employee(self) -> None:
        '''
        Function to update employee's ID.
        '''
        id_genere= generate_id()

        wait_click(self.driver, self.pencil_button)
        
        time.sleep(1)
        old_id_employee = self.id_employee_input.get_attribute('value')

        self.id_employee_input.set_text(id_genere)
        
        new_id_employee = self.id_employee_input.get_attribute('value')

        save_button_list = self.driver.find_elements(By.XPATH, "//button[@type='submit']")

        wait_click(self.driver, save_button_list[0])

        self.update_csv_employee_id(old_id_employee, new_id_employee)