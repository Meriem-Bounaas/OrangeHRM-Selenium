from os.path import join, dirname
from pytest_csv_params.decorator import csv_params

from src.pages.login_page import LoginPage
from src.pages.dashboard_page import DashboardPage

@csv_params(
    data_file="data_login_employees_valid.csv",
    # base_dir=join(dirname(__file__), "assets"),
    data_casts={
        "username": str,
        "password": str
    },
)
def test_login_employee_valid(username: str, password: str, login_page: LoginPage, dashboard_page: DashboardPage) -> None:
    '''
        Test for successful login using a valid username and password.
    '''
    assert login_page.verify_page_title()
    assert login_page.verify_page_url()

    login_page.login(username, password)

    assert dashboard_page.verify_page()