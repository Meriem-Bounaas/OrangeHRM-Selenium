from os.path import join, dirname
from pytest_csv_params.decorator import csv_params

from src.pages.dashboard_page import DashboardPage
from src.pages.login_page import LoginPage
from src.pages.pim_page import PimPage

@csv_params(
    data_file="data_login_valid.csv",
    base_dir=join(dirname(__file__), "assets"),
    data_casts={
        "username": str,
        "password": str
    },
)
def test_add_employee_valid(username: str, password: str, dashboard_page: DashboardPage, pim_page: PimPage, login_page: LoginPage) -> None:
    '''
    Test to add a valid employee.
    '''
    assert login_page.verify_page_title()
    assert login_page.verify_page_url()

    login_page.login(username, password)

    assert dashboard_page.verify_page()

    dashboard_page.go_to_pim_page()

    assert pim_page.verify_page()

    pim_page.click_button_add_employee()

    assert pim_page.verify_existence_of_add_employee_text()

    pim_page.fill_form_employee(True)

    assert pim_page.verify_existence_of_personel_details_text()