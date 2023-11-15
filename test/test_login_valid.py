import pytest

from src.pages.login_page import LoginPage
from src.pages.dashboard_page import DashboardPage

@pytest.mark.parametrize('data', [{'username': 'Admin', 'password': 'admin123'}])
def test_login_valid(data, login_page: LoginPage, dashboard_page: DashboardPage) -> None:
    '''
        Test for successful login using a valid username and password.
    '''
    assert login_page.verify_page_title()
    assert login_page.verify_page_url()

    login_page.login(data['username'], data['password'])

    assert dashboard_page.verify_page()