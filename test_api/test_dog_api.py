import json
import requests
import os
import pytest


def get_path(file_name):
    work_folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(work_folder, file_name)


dog_api_breeds_list = get_path('dog_api_breeds_list')

base_url = 'https://dog.ceo/api/'


def test_get_all_breeds():
    all_breeds = "breeds/list/all"
    url_all_breeds = base_url + all_breeds
    result_all_breeds = requests.get(url_all_breeds)
    assert 200 == result_all_breeds.status_code
    with open(dog_api_breeds_list, "r") as file:
        json_breeds = json.loads(file.read())
        assert json_breeds == result_all_breeds.json()


def test_get_random_image():
    random_image = "breeds/image/random"
    url_random_image = base_url + random_image
    result_random_image = requests.get(url_random_image)
    get_json_image = result_random_image.json()
    print(get_json_image)
    assert 200 == result_random_image.status_code


@pytest.mark.parametrize("param", [3, 49, 50])
def test_get_multiple_random_images(param):
    random_multiple_images = f"breeds/image/random/{param}"
    url_random_multiple_images = base_url + random_multiple_images
    result_multiple_images = requests.get(url_random_multiple_images)
    get_json_images = result_multiple_images.json()
    assert 200 == result_multiple_images.status_code
    return get_json_images


@pytest.mark.parametrize("param", [-10, 0, 51, 0.1])
def test_get_multiple_random_images_negative(param):
    with pytest.raises(ValueError):
        if param < 1 or param > 50:
            raise ValueError("Incorrect parameter, check value ")
    random_multiple_images = f"breeds/image/random/{param}"
    url_random_multiple_images = base_url + random_multiple_images
    result_multiple_images = requests.get(url_random_multiple_images)
    get_json_images = result_multiple_images.json()
    print(get_json_images)
    assert 200 == result_multiple_images.status_code
    return get_json_images


@pytest.mark.parametrize("param", ["text", True, False])
def test_get_multiple_random_images_negative_2(param):
    with pytest.raises(ValueError):
        if param != int:
            raise ValueError("It's not a number, check value ")
    random_multiple_images = f"breeds/image/random/{param}"
    url_random_multiple_images = base_url + random_multiple_images
    result_multiple_images = requests.get(url_random_multiple_images)
    get_json_images = result_multiple_images.json()
    print(get_json_images)
    assert 200 == result_multiple_images.status_code
    return get_json_images
