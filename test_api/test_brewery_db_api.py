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
    assert 200 == result_brew_url.status_code
    if get_json_single["address_1"] is None:
        raise ValueError("address_2 is not None")
    else:
        return get_json_single


@pytest.mark.parametrize("param",
                         ["micro", "nano", "regional", "brewpub", "large", 'planning', "bar", 'contract', 'proprietor',
                          'closed'])
def test_get_brew_by_type(param):
    brew_type = f"?by_type={param}"
    url_brew_type = base_url + brew_type
    result_brew_type = requests.get(url_brew_type)
    assert 200 == result_brew_type.status_code
    get_json_type = result_brew_type.json()
    print(get_json_type)


@pytest.mark.parametrize("pages", [1, 50, 51, 199, 200])
def test_get_users_per_page(pages):
    per_pages = f"?per_page={pages}"
    url_per_pages = base_url + per_pages
    result_per_pages = requests.get(url_per_pages)
    assert 200 == result_per_pages.status_code


@pytest.mark.parametrize("pages", [-1, 0, 201])
def test_get_users_per_page_negative(pages):
    with pytest.raises(ValueError):
        if pages < 1 or pages > 200:
            raise ValueError("Incorrect parameter, check value ")
    per_pages = f"?per_page={pages}"
    url_per_pages = base_url + per_pages
    result_per_pages = requests.get(url_per_pages)
    assert 200 == result_per_pages.status_code
    print(result_per_pages.json())


def test_metadata():
    meta = "/meta"
    url_meta = base_url + meta
    result_url_meta = requests.get(url_meta)
    assert 200 == result_url_meta.status_code
    print(result_url_meta.json())
