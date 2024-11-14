from venv import logger

import requests
from json import JSONDecodeError
from posixpath import join as urljoin
from framework.logging import log_request, log_response
import loguru



def return_json(func):
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        try:
            return response.json()
        except JSONDecodeError:
            return response.text
    return wrapper


class BaseApi:

    def __init__(self):
        self._service_url = "https://petstore.swagger.io/v2"
        self._global_headers = {"api_key": "special-key"}
        self._auth = None

    def update_global_headers(self, headers: dict):
        self._global_headers.update(headers)

    def update_global_auth(self, auth):
        self._auth = auth

    @return_json
    def post(self, handler: str, json=None, data=None, files=None, headers:dict=None, **kwargs):
        request_params = self._make_request_params(headers, handler)
        return self._request(method="POST", json=json, data=data, files=files, **kwargs, **request_params)

    @return_json
    def get(self, handler: str, params:dict=None, headers: dict = None, **kwargs):
        request_params = self._make_request_params(headers, handler)
        return self._request(method="GET", params=params, **kwargs, **request_params)

    @return_json
    def put(self, handler: str, json=None, data=None,  headers: dict = None, **kwargs):
        request_params = self._make_request_params(headers, handler)
        return self._request(method="PUT", json=json, data=data, **kwargs, **request_params)

    @return_json
    def patch(self, handler: str, json=None, data= None,  headers: dict = None, **kwargs):
        request_params = self._make_request_params(headers, handler)
        return self._request(method="PATCH", json=json, data=data, **kwargs, **request_params)

    @return_json
    def delete(self, handler: str, headers: dict = None, **kwargs):
        request_params = self._make_request_params(headers, handler)
        return self._request(method="DELETE", **kwargs, **request_params)

    def _make_request_params(self, headers, handler):
        headers = headers or {}
        resul_header = self._global_headers.copy()
        resul_header.update(headers)
        result_url = urljoin(self._service_url, handler)

        return {"headers": resul_header, "url": result_url}


    def _request(self, method: str, url: str, json=None, files=None, data=None, params:dict=None, headers:dict=None, **_):
        request = requests.Request(method=method, url=url, json=json, files=files, data=data,params=params, headers=headers, auth=self._auth).prepare()
        log_request(logger=loguru.logger, request=request)
        with requests.Session() as session:
            response = session.send(
                request=request, verify=False
            )

        log_response(logger=loguru.logger, response=response)
        return response

class BaseHandlers:
    def __init__(self, client:BaseApi):
        self.client = client