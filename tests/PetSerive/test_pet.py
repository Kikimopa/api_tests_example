from framework.Pet import PetService
from framework.Pet.model.pet import pet

def test_create_new_pet():
	pet_service = PetService()
	response = pet_service.pet.create(pet=pet)

