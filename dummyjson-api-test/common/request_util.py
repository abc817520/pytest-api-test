import requests
from common.yaml_util import get_config


class RequestUtil:
    session = requests.Session()
    base_url = get_config()["base_url"]

    # @classmethod
    # def request(cls, method, url, **kwargs):
    #     url = cls.base_url + url
    #     return cls.session.request(method, url, **kwargs)
    @classmethod
    def request(cls, method, url, headers=None, **kwargs):
        url = cls.base_url + url
        return cls.session.request(
            method,
            url,
            headers=headers,
            **kwargs
        )
    @classmethod
    def get(cls, url, **kwargs):
        return cls.request("GET", url, **kwargs)

    @classmethod
    def post(cls, url, **kwargs):
        return cls.request("POST", url, **kwargs)
