from pathlib import Path
import csv
import os
import time
from selenium.webdriver.support.select import Select
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
        'header_element': ("XPATH", "//*[@id=\"app\"]/div[1]/div[1]/header/div[1]/div[1]/span/h6"),
        'add_button': ("XPATH", "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button"),
        'first_name': ("XPATH", "//*[@name='firstName']"),
        'last_name': ("XPATH", "//*[@name='lastName']"),
        'id_employee': ("XPATH", "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input"),
        'save_button': ("XPATH", "//*[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']"),
        'profile_picture_element': ("XPATH", "//*[@class='employee-image']"),
        'required_element': ("XPATH", "//*[text()='Required']"),
        'search_input': ("XPATH", "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input"),
        'search_button': ("XPATH", "//*[@type='submit']"),
        'reset_button': ("XPATH", "//*[@type='submit']"),
        'create_login_detail_button': ("XPATH", "//*[@class='oxd-switch-input oxd-switch-input--active --label-right']"),
        'username_input': ("XPATH", "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input"),
        'password_input': ("XPATH", "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input"),
        'confirm_password_input': ("XPATH", "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input"),
        'my_info_button': ("XPATH", "//*[@href= '/web/index.php/pim/viewMyDetails']"),
        'personal_details_button': ("XPATH", ".//a[contains(@href, '/web/index.php/pim/viewPersonalDetails')]"),
        'contact_details_button': ("XPATH", ".//a[contains(@href, '/web/index.php/pim/contactDetails')]"),
        'header_form_employee_element': ("XPATH", "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6"),
        'marital_status_list': ("XPATH", "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div"),
        'marital_status_folowing_sibling': ("XPATH", "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/following-sibling::div"),
        'blood_type_list': ("XPATH", "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div"),
        'pencil_button': ("XPATH", "//*[@class='oxd-icon bi-pencil-fill']"),
        'id_employee_input': ("XPATH", "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[1]/div/div[2]/input"),
        'save_personal_detail_button': ("XPATH", "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button")
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
        return bool(self.required_element)

    def click_button_add_employee(self) -> None:
        '''
        Function to click the 'Add' button for adding an employee.
        '''
        self.add_button.click_button()

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
            self.first_name.set_text(first_name)
            self.last_name.set_text(last_name)
            self.id_employee.set_text(id_employee)

            self.create_login_detail_button.click_button()

            self.username_input.set_text(user_name)
            self.password_input.set_text(password)
            self.confirm_password_input.set_text(password)

            self.save_button.click_button()

            self.save_data_csv('data_login_employees_valid.csv', [
                               'username', 'password'], [user_name, password])
            self.save_data_csv('data_employees_informations.csv', ['id_employee', 'first_name', 'last_name', 'username', 'password'], [
                               id_employee, first_name, last_name, user_name, password])

        else:
            self.id_employee.set_text(generate_id())
            self.save_button.click_button()

        time.sleep(5)

    def search_employee_by_id(self) -> object:
        '''
        Function to search an employee using ID.
        '''
        table_employee = self.driver.find_elements(
            By.XPATH, "//*[@class='oxd-table-card']")
        employee_row = random.choice(table_employee)

        id_employee = employee_row.text.splitlines()[0]
        first_name = employee_row.text.splitlines()[1]
        last_name = employee_row.text.splitlines()[2]

        self.reset_button.click_button()
        self.search_input.set_text(id_employee)
        self.search_button.click_button()

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

    def go_to_my_info(self) -> None:
        '''
        Function to click and access the details information page about an employee.
        '''
        self.my_info_button.click_button()

    def go_to_personal_details(self) -> None:
        '''
        Function to click and access an employee's personal details.
        '''
        self.personal_details_button.click_button()

    def go_to_contcat_details(self) -> None:
        '''
        Function to click and access an employee's contact details.
        '''
        self.contact_details_button.click_button()

    def verify_header_form_personal_details(self) -> bool:
        '''
        Function to verify the header of the personal details form..
        '''
        return verify_header_of_my_info_page(self.header_form_employee_element, 'Personal Details')

    def verify_header_form_contact_details(self) -> bool:
        '''
        Function to verify the header of the contact details form.
        '''
        return verify_header_of_my_info_page(self.header_form_employee_element, 'Contact Details')

    def insert_into_personal_details(self) -> None:
        '''
        Function to insert marital status, blood type and gender in the personal details form.
        '''
        # TODO
        marital_status = ["Single", "Married", "Other"]
        # drop = Select(self.marital_status_list)
        # drop.select_by_visible_text(random.choice(marital_status))

        self.marital_status_list.click_button()
        print('zzzzzzzzz', self.marital_status_folowing_sibling.get_attribute('innerHTML'))

        time.sleep(2)

        # self.blood_type_list.click_button()
        # self.gender_button.click_button()

        self.save_button.click_button()

    def insert_into_contact_details(self) -> None:
        '''
        Function to insert city, zip code and email in the contact details form.
        '''
        self.city_input.set_text(generate_city())
        self.zip_input.set_text(generate_zip())
        self.email_input.set_text(generate_email())

        self.save_button.click_button()

    def upadate_csv_employee_id(self, old_id, new_id):
        pass

    def update_id_employee(self) -> None:
        '''
        Function to update employee's ID.
        '''
        id_employee = generate_id()

        self.pencil_button.click_button()
        old_id_employee = self.id_employee_input.text

        self.id_employee_input.clear()
        self.id_employee_input.set_text(id_employee)

        self.save_personal_detail_button.click_button()

        #  TODO: update in csv file the new ID
        self.update_csv_employee_id(old_id_employee, id_employee)
