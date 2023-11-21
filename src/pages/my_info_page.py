import time
from selenium.webdriver.edge.webdriver import WebDriver

from src.base.base_page import BasePage
from utils.common import *


class MyinfoPage(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    locators = {
        'pencil_button': ("XPATH", "//*[@class='oxd-icon bi-pencil-fill']"),
        'id_employee_input': ("XPATH", "//*[contains(text(),'Employee Id')]/parent::div/following-sibling::div/input"),
        'my_info_button': ("XPATH", "//*[@href= '/web/index.php/pim/viewMyDetails']"),
        'contact_details_button': ("XPATH", ".//a[contains(@href, '/web/index.php/pim/contactDetails')]"),
        'personal_details_button': ("XPATH", ".//a[contains(@href, '/web/index.php/pim/viewPersonalDetails')]"),
        'marital_status_element': ("XPATH", "//label[text()= 'Marital Status']/parent::div/following-sibling::div/child::div/child::div"),
        'marital_status_list': ("XPATH", "//label[text()= 'Marital Status']/parent::div/following-sibling::div/child::div/child::div/preceding-sibling::div"),
        'save_personal_detail_button': ("XPATH", "//div[@class = 'oxd-form-actions']/descendant::button/preceding-sibling::p/following-sibling::button"),
        'header_form_employee': ("XPATH", "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6")
    }

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
        return verify_header_of_my_info_page(self.header_form_employee, 'Personal Details')

    def verify_header_form_contact_details(self) -> bool:
        '''
        Function to verify the header of the contact details form.
        '''
        return verify_header_of_my_info_page(self.header_form_employee, 'Contact Details')

    def insert_into_personal_details(self) -> None:
        '''
        Function to insert marital status, blood type and gender in the personal details form.
        '''
        # TODO :
        self.marital_status_element.click_button()
        # print('zzzzzzzzz', self.marital_status_list.text)
        print('zzzzzzzzz', self.marital_status_list.get_attribute('innerHTML'))

        time.sleep(2)

        # self.blood_type_list.click_button()
        # self.gender_button.click_button()

        # self.save_button.click_button()

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
        # self.update_csv_employee_id(old_id_employee, id_employee)
