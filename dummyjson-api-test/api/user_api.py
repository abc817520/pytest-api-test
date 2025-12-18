from common.request_util import RequestUtil
from common.token_manager import TokenManager

class UserApi:

    def get_user_info(self):
        headers = TokenManager.get_auth_headers()
        return RequestUtil.get("/auth/me", headers=headers)
