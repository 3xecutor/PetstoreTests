import pytest
import requests

import data

@pytest.fixture
def pet_id():
    return 450198289


@pytest.fixture
def pet_url(pet_id):
    return f"https://petstore.swagger.io/v2/pet/{pet_id}"


@pytest.fixture
def pet_headers():
    return {"accept": "application/json"}


@pytest.fixture
def expected_pet_data(pet_id):
    return {"id": pet_id, "name": "gold", "status": "available"}


@pytest.mark.parametrize("pet_id,expected_pet_data", [(450198289,
                                                       hh.get_pet)])
def test_get_pet_by_id(pet_id, pet_url, pet_headers, expected_pet_data):
    response = requests.get(pet_url, headers=pet_headers)
    assert response.status_code == 200
    response = requests.get(pet_url, headers=pet_headers)
    assert response.json() == expected_pet_data
