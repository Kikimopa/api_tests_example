from random import randint

from faker import Faker

faker = Faker()

pet = {
"id": randint(1, 999),
  "category": {
    "id": randint(1, 999),
    "name": faker.name()
  },
  "name": faker.name(),
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": randint(1, 999),
      "name": faker.name()
    }
  ],
  "status": "available"
}