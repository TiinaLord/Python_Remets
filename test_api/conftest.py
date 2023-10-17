import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--base_url", default="https://ya.ru/", help="base_url"
    )
    parser.addoption(
        "--status_code_200", default=200, help="Status code - 200"
    )
    parser.addoption(
        "--status_code_404", default=404, help="Status code - 404"
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--base_url")


@pytest.fixture
def status_code_200(request):
    return request.config.getoption("--status_code_200")


@pytest.fixture
def status_code_404(request):
    return request.config.getoption("--status_code_404")
