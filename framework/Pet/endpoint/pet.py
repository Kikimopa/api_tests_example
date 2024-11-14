from http import HTTPStatus

from framework.base_api import BaseHandlers


class PetHandlers(BaseHandlers):

    def create(self, pet, **kwargs):
        handler = "pet"
        kwargs.setdefault("_ex_status_code", HTTPStatus.OK)
        return self.client.post(handler=handler, json=pet, **kwargs)
