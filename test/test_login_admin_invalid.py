from os.path import join, dirname
from pytest_csv_params.decorator import csv_params

from src.pages.login_page import LoginPage

@csv_params(
    data_file="data_login_admin_invalid.csv",
    base_dir=join(dirname(__file__), "assets"),
    data_casts={
        "username": str,
        "password": str
    },
)
def test_login_admin_invalid(username: str, password: str, login_page: LoginPage) -> None:
    '''
        Test for failed login using invalid username and password.
    '''
    assert login_page.verify_page_title
    assert login_page.verify_page_url
    
    login_page.login(username, password)

    assert login_page.invalid_credentials  