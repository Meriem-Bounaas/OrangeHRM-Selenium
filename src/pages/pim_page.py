import csv
import os

from os.path import join, dirname
from pytest_csv_params.decorator import csv_params

from src.base.base_page import BasePage
from selenium.webdriver.edge.webdriver import WebDriver

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
        'personel_details_element': ("XPATH", "//*[text()='Personal Details']"),
        'required_element': ("XPATH", "//*[text()='Required']"),
        'table_employee': ("XPATH", "//*[@class='oxd-table-card']")
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
    
    def verify_existence_of_personel_details_text(self) -> bool: 
        '''
        Function to verify the existence of the text 'Personel Details' on the page.
        '''
        return bool(self.personel_details_element)
    
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

    def fill_form_employee(self, with_username) -> None:
        '''
        Function to populate the employee form.
        '''
        first_name = generate_first_name()
        last_name = generate_last_name()
        id_employee = generate_id()

        if with_username:
            self.first_name.set_text(first_name)
            self.last_name.set_text(last_name)
            self.id_employee.set_text(id_employee)
            self.save_button.click_button()

            # file_exists = os.path.isfile('employee_data.csv')
            # with open('employee_data.csv', 'a', newline='') as file:
            #     writer = csv.writer(file)
            #     if not file_exists:
            #         writer.writerow(["id", "first_name","last_name"])
            #     writer.writerow([id_employee, first_name, last_name])

        else:
            self.id_employee.set_text(generate_id())
            self.save_button.click_button()

    def search_employee_by_id(self) -> None:
        '''
        Function to search an employee using ID.
        '''
    #  TODO : read from table employee une ligne au hasard
        # print(self.table_employee)
        # employee_row = random.choice(self.table_employee)
        # print('employeeeee'+ employee_row)

    #  TODO : save id , firstname, generate_last_name
    #  TODO : search by id , click search
  

    # def verify_existing_of_one_employee(self) -> None:
    #     pass
    # // TODO : test length is one ligne 
    # // TODO : test the best firsname et lastname 
