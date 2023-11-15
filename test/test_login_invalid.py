import pytest

from src.pages.login_page import LoginPage

@pytest.mark.parametrize('data', [{'username': 'admin', 'password': ''},
                                  {'username': '', 'password': 'admin123'},
                                  {'username': 'admin', 'password': 'admin'},
                                  {'username': '', 'password': ''}])
def test_login_invalid(data, login_page: LoginPage) -> None:
    '''
        Test for failed login using invalid username and password.
    '''
    assert login_page.verify_page_title
    assert login_page.verify_page_url
    
    login_page.login(data['username'], data['password'])

    assert login_page.invalid_credentials  