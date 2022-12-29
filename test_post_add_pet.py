import json

import jsonschema
import pytest
import requests


@pytest.fixture
def create_pet():
    def _create_pet(method, pet_data):
        api_url = "https://petstore.swagger.io/v2/pet"
        headers = {
            "Accept": "application/json",
            "Content-type": "application/json"
        }
        response = requests.request(
            method, api_url, json=pet_data, headers=headers)
        return response

    return _create_pet


@pytest.fixture
def pet_data():
    return {
        "id": 450198289,
        "category": {
            "id": 1,
            "name": "Tests"
        },
        "name": "Gold",
        "photoUrls": [
            "https://vk.com/cute.jpg"
        ],
        "tags": [
            {
                "id": 450198289,
                "name": "Cute"
            }
        ],
        "status": "available"
    }


@pytest.fixture
def expected_schema():
    return {
        "type": "object",
        "properties": {
            "id": {"type": "integer", "format": "int64"},
            "category": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer", "format": "int64"},
                    "name": {"type": "string"}
                }
            },
            "name": {"type": "string"},
            "photoUrls": {
                "type": "array",
                "items": {"type": "string"}
            },
            "tags": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer", "format": "int64"},
                        "name": {"type": "string"}
                    }
                }
            },
            "status": {"type": "string", "enum": ["available", "pending", "sold"]}
        }
    }


def test_create_pet(create_pet, pet_data, expected_schema):
    response = create_pet("POST", pet_data)
    response_data = json.loads(response.text)
    validation_errors = jsonschema.validate(response_data, expected_schema)
    assert response.status_code == 200
    assert not validation_errors, f"Validation errors: {validation_errors}"
