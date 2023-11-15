import pytest

from src.pages.dashboard_page import DashboardPage
from src.pages.login_page import LoginPage
from src.pages.pim_page import PimPage

@pytest.mark.parametrize('data', [{'username': 'Admin', 'password': 'admin123'}])
def test_add_employee_valid(data, dashboard_page: DashboardPage, pim_page: PimPage, login_page: LoginPage) -> None:
    '''
    Test to add a valid employee.
    '''
    assert login_page.verify_page_title()
    assert login_page.verify_page_url()

    login_page.login(data['username'], data['password'])

    assert dashboard_page.verify_page()

    dashboard_page.go_to_PIM_page()

    assert pim_page.verify_page()

    pim_page.click_button_add_employee()

    assert pim_page.verify_existence_of_add_employee_text()

    pim_page.fill_form_employee()

    assert pim_page.verify_existence_of_personel_details_text()