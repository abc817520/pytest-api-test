from api.auth_api import AuthApi
from common.yaml_util import get_config

from api.auth_api import AuthApi

class TokenManager:
    _token = None

    @classmethod
    def get_token(cls):
        if cls._token is None:
            res = AuthApi().login(
                username=get_config()["username"],
                password=get_config()["password"]
            )
            cls._token = res.json().get("accessToken")
        return cls._token

    @classmethod
    def get_auth_headers(cls):
        token = cls.get_token()
        return {
            "Authorization": f"Bearer {token}"
        }