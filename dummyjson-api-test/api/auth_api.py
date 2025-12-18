from common.request_util import RequestUtil

class AuthApi:

    def login(self, username, password):
        data = {
            "username": username,
            "password": password
        }
        return RequestUtil.post(
            "/auth/login",
            json=data
        )
