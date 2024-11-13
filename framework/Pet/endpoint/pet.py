from framework.base_api import BaseHandlers

class PetHandlers(BaseHandlers):

	def create(self, pet, **kwargs):
		handler = "pet"
		return self.client.post(handler=handler, json=pet, **kwargs)