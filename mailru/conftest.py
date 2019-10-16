import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    # предполагается что драйвер прописан в путях операцинной системы иначе надо указать полный путь до него
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
    return driver


def pytest_addoption(parser):
    """
    parser.addoption
    :param parser:
    :return:
    """
    parser.addoption("--login", action="store", default="login", help="login to mail.ru - email without '@mail.ru'")
    parser.addoption("--password", action="store", default="123456", help="password")


@pytest.fixture
def password(request):
    """
    fixture returns password in params
    :param request:
    :return:
    """
    return request.config.getoption("--password")


@pytest.fixture
def login(request):
    """
    fixture return value of login passed in params
    :param request:
    :return:
    """
    return request.config.getoption("--login")
