import pytest
from selenium.webdriver.edge.webdriver import WebDriver

from src.pages.login_page import LoginPage
from src.pages.dashboard_page import DashboardPage

@pytest.mark.parametrize('data', [{'username': 'Admin', 'password': 'admin123'}])
def test_login_valid(browser: WebDriver, data, login_page: LoginPage, dashboard_page: DashboardPage) -> None:
    assert login_page.verify_page_title()
    assert login_page.verify_page_url()

    login_page.login(data['username'], data['password'])

    assert dashboard_page.verify_page()