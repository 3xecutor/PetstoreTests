import pytest
import requests

@pytest.fixture
def pet_id():
    return 450198289


@pytest.fixture
def pet_url(pet_id):
    return f"https://petstore.swagger.io/v2/pet/{pet_id}"


@pytest.fixture
def pet_headers():
    return {"accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"}


def test_post_pet_id(pet_url, pet_headers):
    data = {"name": "gold", "status": "available"}
    response = requests.post(pet_url, headers=pet_headers, data=data)
    assert response.status_code == 200
