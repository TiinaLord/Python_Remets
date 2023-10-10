import requests
import pytest


def test_get_200(base_url, status_code_200):
    result = requests.get(base_url)
    assert status_code_200 == result.status_code


@pytest.mark.parametrize("endpoint", ["delete//", 0, False, 0.1, -1])
def test_get_404(base_url, status_code_404, endpoint):
    result = requests.get(f"{base_url}/{endpoint}")
    assert status_code_404 == result.status_code
