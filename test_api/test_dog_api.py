import json
import requests
import os
import pytest


def get_path(file_name):
    work_folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(work_folder, file_name)


dog_api_breeds_list = get_path('dog_api_breeds_list')

base_url = 'https://dog.ceo/api/'


@pytest.fixture()
def expected_breeds():
    with open(dog_api_breeds_list, "r") as file:
        json_breeds = json.loads(file.read())
    return json_breeds


def test_get_all_breeds(expected_breeds):
    all_breeds = "breeds/list/all"
    url_all_breeds = base_url + all_breeds
    result_all_breeds = requests.get(url_all_breeds)
    assert result_all_breeds.status_code == 200
    assert result_all_breeds.json() == expected_breeds


def test_get_random_image():
    random_image = "breeds/image/random"
    url_random_image = base_url + random_image
    result_random_image = requests.get(url_random_image)
    get_json_image = result_random_image.json()
    print(get_json_image)
    assert result_random_image.status_code == 200


@pytest.mark.parametrize("random_img", [3, 49, 50])
def test_get_multiple_random_images(random_img):
    random_multiple_images = f"breeds/image/random/{random_img}"
    url_random_multiple_images = base_url + random_multiple_images
    result_multiple_images = requests.get(url_random_multiple_images)
    get_json_images = result_multiple_images.json()
    assert result_multiple_images.status_code == 200
    print(get_json_images)
    assert random_img == len(get_json_images["message"])

@pytest.mark.parametrize("random_img", [-10, 0, 51, 0.1])
def test_get_multiple_random_images_negative(random_img):
    random_multiple_images = f"breeds/image/random/{random_img}"
    url_random_multiple_images = base_url + random_multiple_images
    result_multiple_images = requests.get(url_random_multiple_images)
    get_json_images = result_multiple_images.json()
    print(get_json_images)
    assert result_multiple_images.status_code == 400


@pytest.mark.parametrize("random_img", ["text", True, False])
def test_get_multiple_random_images_negative_2(random_img):
    random_multiple_images = f"breeds/image/random/{random_img}"
    url_random_multiple_images = base_url + random_multiple_images
    result_multiple_images = requests.get(url_random_multiple_images)
    get_json_images = result_multiple_images.json()
    print(get_json_images)
    assert result_multiple_images.status_code == 400
