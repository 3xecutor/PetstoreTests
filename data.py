get_pet = {'id': 450198289, 'category': {'id': 1, 'name': 'Tests'}, 'name': 'Gold',
           'photoUrls': ['https://vk.com/cute.jpg'], 'tags': [{'id': 450198289, 'name': 'Cute'}], 'status': 'available'}

put_e = {"id": 2, "category": {"id": 2, "name": "Cats"}, "name": "Whiskers", "photoUrls": ["https://vk.com/cute.jpg"],
         "tags": [{"id": 2, "name": "Playful"}], "status": "pending"}

put_i = {"id": 1, "category": {"id": 1, "name": "Dogs"}, "name": "Fluffy", "photoUrls": ["https://vk.com/cute.jpg"],
         "tags": [{"id": 1, "name": "Cute"}], "status": "available"}

e_schema = {"type": "object", "properties": {"id": {"type": "integer", "format": "int64"},
                                             "category": {"type": "object",
                                                          "properties": {"id": {"type": "integer", "format": "int64"},
                                                                         "name": {"type": "string"}}},
                                             "name": {"type": "string"},
                                             "photoUrls": {"type": "array", "items": {"type": "string"}},
                                             "tags": {"type": "array", "items": {"type": "object", "properties": {
                                                 "id": {"type": "integer", "format": "int64"},
                                                 "name": {"type": "string"}}}},
                                             "status": {"type": "string", "enum": ["available", "pending", "sold"]}}}

p_data = {"id": 450198289, "category": {"id": 1, "name": "Tests"}, "name": "Gold",
          "photoUrls": ["https://vk.com/cute.jpg"], "tags": [{"id": 450198289, "name": "Cute"}], "status": "available"}
