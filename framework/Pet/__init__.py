from framework.base_api import BaseApi
from framework.Pet.endpoint.pet import PetHandlers

class PetService(BaseApi):
	def __init__(self):
		super().__init__()

		self.pet: PetHandlers = PetHandlers(self)