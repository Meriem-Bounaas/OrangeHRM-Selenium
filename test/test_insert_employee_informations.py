from pytest_csv_params.decorator import csv_params

from src.pages.login_page import LoginPage
from src.pages.dashboard_page import DashboardPage
from src.pages.pim_page import PimPage

@csv_params(
    data_file="data_login_employees_valid.csv",
    # base_dir=join(dirname(__file__), "assets"),
    data_casts={
        "username": str,
        "password": str
    },
)
def test_login_employee_valid(username: str, password: str, login_page: LoginPage, dashboard_page: DashboardPage, pim_page: PimPage) -> None:
    '''
        Test for successful login using a valid username and password.
    '''
    assert login_page.verify_page_title()
    assert login_page.verify_page_url()

    login_page.login(username, password)

    assert dashboard_page.verify_page()

    pim_page.go_to_my_info()

    assert pim_page.verify_existence_of_profile_picture()

    pim_page.go_to_personal_details()

    assert pim_page.verify_header_form_personal_details()

    pim_page.insert_into_personal_details()
    
    # TODO : assert sucess update

    pim_page.go_to_contcat_details()

    assert pim_page.verify_header_form_contact_details()

    pim_page.insert_into_contact_details()

    # TODO : assert sucess update