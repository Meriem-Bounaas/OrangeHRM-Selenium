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
        'personel_details_element': ("XPATH", "//*[text()='Personal Details']")
    }

    def verify_page(self) -> bool:
        '''
        Function to verify url and title and header of the dashboard login.
        '''
        return super().verify_url(self.url) and super().verify_title(self.title) and super().verify_header(self.header_element, self.header)
    
    def verify_existence_of_add_employee_text(self) -> bool: 
        '''
        Function to verify the existence of the text 'add employee' on the page
        '''
        return bool(self.save_button)
    
    def verify_existence_of_personel_details_text(self) -> bool: 
        '''
        Function to verify the existence of the text 'Personel Details' on the page
        '''
        return bool(self.personel_details_element)
    
    def click_button_add_employee(self):
        '''
        Function to click the 'Add' button for adding an employee.
        '''
        self.add_button.click_button()

    def fill_form_employee(self):
        '''
        Function to populate the employee form.
        '''
        self.first_name.set_text(generate_first_name())
        self.last_name.set_text(generate_last_name())
        self.id_employee.set_text(generate_id())
        self.save_button.click_button()