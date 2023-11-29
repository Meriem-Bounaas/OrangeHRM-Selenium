from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By

from src.base.base_page import BasePage
from utils.common import *

class MyinfoPage(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    locators = {
        'id_employee_input': ("XPATH", "//*[contains(text(),'Employee Id')]/parent::div/following-sibling::div/input"),
        'my_info_button': ("XPATH", "//*[@href= '/web/index.php/pim/viewMyDetails']"),
        'contact_details_button': ("XPATH", ".//a[contains(@href, '/web/index.php/pim/contactDetails')]"),
        'personal_details_button': ("XPATH", ".//a[contains(@href, '/web/index.php/pim/viewPersonalDetails')]"),
        'marital_status_element': ("XPATH", "//label[text()= 'Marital Status']/parent::div/following-sibling::div/child::div/child::div"),
        'blood_type_element': ("XPATH", "//label[text()= 'Blood Type']/parent::div/following-sibling::div/child::div/child::div"),
        'blood_type_list': ("XPATH", "//label[text()= 'Blood Type']/parent::div/following-sibling::div"),
        'save_personal_detail_button': ("XPATH", "//div[@class = 'oxd-form-actions']/descendant::button/preceding-sibling::p/following-sibling::button"),
        'header_form_employee': ("XPATH", "//div[@class= 'orangehrm-edit-employee-content']/div[1]/h6"),
        'toaster_success': ("XPATH", "//*[@class='oxd-toast oxd-toast--success oxd-toast-container--toast']"),
        'city_input': ("XPATH", "//label[text()= 'City']/parent::div/following-sibling::div/input"),
        'zip_input': ("XPATH", "//label[text()= 'Zip/Postal Code']/parent::div/following-sibling::div/input"),
        'email_input': ("XPATH", "//label[text()= 'Work Email']/parent::div/following-sibling::div/input"),
        'save_button': ("XPATH", '//button[@type="submit"]')
    }

    def go_to_my_info(self) -> None:
        '''
        Function to click and access the details information page about an employee.
        '''
        wait_click(self.driver, self.my_info_button)

    def go_to_personal_details(self) -> None:
        '''
        Function to click and access an employee's personal details.
        '''
        wait_click(self.driver, self.personal_details_button)

    def go_to_contact_details(self) -> None:
        '''
        Function to click and access an employee's contact details.
        '''
        wait_click(self.driver, self.contact_details_button)

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
    
    def verify_toaster_success(self) -> bool:
        '''
        Function to verify the appearance of toaster success.
        '''
        return bool(self.toaster_success)

    def insert_marital_status_and_gender_into_personal_details(self) -> None:
        '''
        Function to insert marital status and gender in the personal details form.
        '''
        wait_click(self.driver, self.marital_status_element)
        marital_status_option_list = self.driver.find_elements(By.XPATH, "//*[@class = 'oxd-select-option']")
        wait_click(self.driver, marital_status_option_list[random.randint(1,3)])

        gender_radio_button = self.driver.find_element(By.XPATH, f"//*[@class = '--gender-grouped-field']/div[{random.choice([1,2])}]")
        wait_click(self.driver, gender_radio_button)

        save_button_list = self.driver.find_elements(By.XPATH, "//button[@type='submit']")

        wait_click(self.driver, save_button_list[0])

    def insert_blood_type_into_personal_details(self) -> None:
        '''
        Function to insert blood type in the personal details form.
        '''
        save_button_list = self.driver.find_elements(By.XPATH, "//button[@type='submit']")

        wait_click(self.driver, self.blood_type_element)
        blood_option_list = self.driver.find_elements(By.XPATH, "//*[@class = 'oxd-select-option']")
        blood_option = blood_option_list[random.randint(1,8)]
        wait_click(self.driver, blood_option)

        wait_click(self.driver, save_button_list[1])
        
    def insert_into_contact_details(self) -> None:
        '''
        Function to insert city, zip code and email in the contact details form.
        '''
        self.city_input.set_text(generate_city())
        self.zip_input.set_text(generate_zip())
        self.email_input.set_text(generate_email())

        wait_click(self.driver, self.save_button)