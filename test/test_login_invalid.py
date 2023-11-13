import pytest
from selenium.webdriver.edge.webdriver import WebDriver


@pytest.mark.smoke
@pytest.mark.parametrize('data', [{'email': 'CRM@gmail.com', 'psw': ''},
                                  {'email': '', 'psw': 'password'},
                                  {'email': 'CRM2', 'psw': 'password'},
                                  {'email': '', 'psw': ''}])
def test_login_invalid(browser: WebDriver, data, login_page: LoginPage) -> None:
    assert login_page.verify_page_title
    assert login_page.verify_page_url
    
    login_page.login(data['email'], data['psw'])




