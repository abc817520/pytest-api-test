import pytest
from common.token_manager import TokenManager

@pytest.fixture(scope="session")
def login():
    """
    session 级别登录
    """
    token = TokenManager.get_token()
    # print(f"获取到的 token: {token}")
    assert token is not None
    return token
