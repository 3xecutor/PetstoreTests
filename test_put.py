import allure
import pytest
import requests

import data


@allure.feature("Pet Management")
@pytest.mark.parametrize("test_input, expected_output", [
    (data.put_i, 200),
    (data.put_e, 200)
])
def test_put_pet(test_input, expected_output):
    url = "https://petstore.swagger.io/v2/pet"
    response = requests.put(url, json=test_input)
    assert response.status_code == expected_output
    assert response.json() == test_input
