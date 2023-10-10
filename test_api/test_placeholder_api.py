import random
import requests
import pytest

base_url = "https://jsonplaceholder.typicode.com/"


@pytest.mark.parametrize("ids", [1, 20, 100])
def test_get_user_by_ids(ids):
    users_id = f"posts/{ids}"
    url_user = base_url + users_id
    result_user = requests.get(url_user)
    assert 200 == result_user.status_code
    print(result_user.json())


def test_post_resource():
    send_post = "posts"
    post_url = base_url + send_post
    json_for_post = {
        "body": {
            "title": "This is testing POST method",
            "body": "Test body",
            "userId": random.randint(101, 1000)
        }
    }
    result_post = requests.post(post_url, json=json_for_post)
    assert 201 == result_post.status_code
    print(result_post.json())


@pytest.mark.parametrize("ids", [5, 50, 99])
def test_put_resource(ids):
    put_resource = f"posts/{ids}"
    url_put = base_url + put_resource
    json_for_put = {
        "body": {
            "id": f"{ids}",
            "title": "This is testing PUT method",
            "body": "Test body",
            "userId": 1
        }
    }
    result_put = requests.put(url_put, json=json_for_put)
    assert 200 == result_put.status_code
    print(result_put.json())


def test_patch_resource():
    patch_resource = "posts/1"
    url_patch = base_url + patch_resource
    json_for_put = {
        "body": {
            "title": "This is testing PATCH method.",
        }
    }
    result_put = requests.put(url_patch, json=json_for_put)
    assert 200 == result_put.status_code
    print(result_put.json())


def test_delete_resource():
    delete_resource = "posts/1"
    url_delete = base_url + delete_resource
    result_delete = requests.delete(url_delete)
    assert 200 == result_delete.status_code
    print(result_delete.json())
