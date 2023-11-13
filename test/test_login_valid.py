import pytest
from selenium.webdriver.edge.webdriver import WebDriver

from src.pages.login_page import LoginPage
from src.pages.dashboard_page import DashboardPage

import time


# @pytest.mark.regression
@pytest.mark.parametrize('data', [{'email': 'Admin', 'psw': 'admin123'}])
def test_login_valid(browser: WebDriver, data, login_page: LoginPage, dashboard_page: DashboardPage) -> None:
    assert login_page.verify_page_title
    assert login_page.verify_page_url

    login_page.login(data['email'], data['psw'])

    time.sleep(5)

    assert dashboard_page.verify_page_title()
    assert dashboard_page.verify_page_url()