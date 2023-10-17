import requests
import pytest

base_url = "https://api.openbrewerydb.org/v1/breweries"


@pytest.mark.parametrize("user_id", ["b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0", "d6317b33-57b6-4509-b4f8-d96094716eef"])
def test_get_single_brewery(user_id):
    odb_id = f"/{user_id}"
    single_brew_url = base_url + odb_id
    result_brew_url = requests.get(single_brew_url)
    get_json_single = result_brew_url.json()
    print(get_json_single)
    assert result_brew_url.status_code == 200
    if get_json_single["address_1"] is None:
        assert "address_1" in get_json_single


@pytest.mark.parametrize("brew_type",
                         ["micro", "nano", "regional", "brewpub", "large", 'planning', "bar", 'contract', 'proprietor',
                          'closed'])
def test_get_brew_by_type(brew_type):
    brew_type_endpoint = f"?by_type={brew_type}"
    url_brew_type = base_url + brew_type_endpoint
    result_brew_type = requests.get(url_brew_type)
    assert result_brew_type.status_code == 200
    get_json_type = result_brew_type.json()
    print(get_json_type)
    for brewery_type in get_json_type:
        assert brew_type == brewery_type['brewery_type']


@pytest.mark.parametrize("pages", [1, 50, 51, 199, 200])
def test_get_users_per_page(pages):
    per_pages = f"?per_page={pages}"
    url_per_pages = base_url + per_pages
    result_per_pages = requests.get(url_per_pages)
    assert result_per_pages.status_code == 200
    assert pages == len(result_per_pages.json())


@pytest.mark.parametrize("pages", [-1, 0, 201])
def test_get_users_per_page_negative(pages):
    per_pages = f"?per_page={pages}"
    url_per_pages = base_url + per_pages
    result_per_pages = requests.get(url_per_pages)
    assert result_per_pages.status_code == 400


def test_metadata():
    meta = "/meta"
    url_meta = base_url + meta
    result_url_meta = requests.get(url_meta)
    assert result_url_meta.status_code == 200
    print(result_url_meta.json())
