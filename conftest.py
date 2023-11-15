from typing import Iterator

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from src.pages.login_page import LoginPage
from src.pages.dashboard_page import DashboardPage
from src.pages.pim_page import PimPage


def pytest_addoption(parser) -> None:
    parser.addoption(
        "--browser-type", action="store", default="edge", help="options: chrome, edge, firefox"
    )


@pytest.fixture(scope='module')
def browser_type(request) -> str:
    return request.config.getoption("--browser-type")


@pytest.fixture(scope='module')
def browser(browser_type: str, request) -> Iterator[WebDriver]:
    if browser_type == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()))
    elif browser_type == 'firefox':
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()))
    else:
        driver = webdriver.Edge(service=EdgeService(
            EdgeChromiumDriverManager().install()))

    driver.implicitly_wait(5)
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call) -> None:
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        if 'browser' in item.fixturenames:
            web_driver = item.funcargs['browser']
        else:
            print('Failed to find web driver')
            return

        # Attach a screenshot if a test failed
        allure.attach(
            web_driver.get_screenshot_as_png(),
            name='screenshot',
            attachment_type=allure.attachment_type.PNG
        )


@pytest.fixture()    
def login_page(browser: WebDriver) -> LoginPage:
    login = LoginPage(browser)
    yield login

@pytest.fixture() 
def dashboard_page(browser: WebDriver) -> DashboardPage:
    dashboard = DashboardPage(browser)
    yield dashboard

@pytest.fixture() 
def pim_page(browser: WebDriver) -> PimPage:
    pim = PimPage(browser)
    yield pim