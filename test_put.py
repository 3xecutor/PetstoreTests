import pytest
import allure
import requests

@allure.feature("Pet Management")
@pytest.mark.parametrize("test_input, expected_output", [
    ({
        "id": 1,
        "category": {
            "id": 1,
            "name": "Dogs"
        },
        "name": "Fluffy",
        "photoUrls": [
            "https://vk.com/cute.jpg"
        ],
        "tags": [
            {
                "id": 1,
                "name": "Cute"
            }
        ],
        "status": "available"
    }, 200),
    ({
        "id": 2,
        "category": {
            "id": 2,
            "name": "Cats"
        },
        "name": "Whiskers",
        "photoUrls": [
            "https://vk.com/cute.jpg"
        ],
        "tags": [
            {
                "id": 2,
                "name": "Playful"
            }
        ],
        "status": "pending"
    }, 200)
])
def test_put_pet(test_input, expected_output):
    url = "https://petstore.swagger.io/v2/pet"
    response = requests.put(url, json=test_input)
    assert response.status_code == expected_output
    assert response.json() == test_input
