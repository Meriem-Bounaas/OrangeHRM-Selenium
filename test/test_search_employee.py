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
def test_search_employee_valid(username: str, password: str, dashboard_page: DashboardPage, pim_page: PimPage, login_page: LoginPage) -> None:
    '''
    Test to search an employee with ID.
    '''
    assert login_page.verify_page_title()
    assert login_page.verify_page_url()

    login_page.login(username, password)

    assert dashboard_page.verify_page()

    dashboard_page.go_to_pim_page()

    assert pim_page.verify_page()

    pim_page.search_employee_by_id()

    # TODO : assert pim_page.verify_existing_of_one_employee()