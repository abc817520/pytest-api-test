import pytest
import allure
from api.auth_api import AuthApi
from common.yaml_util import load_test_data

@allure.feature("认证模块")
@allure.story("用户登录")
@pytest.mark.parametrize(
    "case",
    load_test_data("auth.yaml", "login")
)
def test_login(case):
    res = AuthApi().login(
        username=case["username"],
        password=case["password"]
    )

    assert res.status_code == case["expect_status"]

    data = res.json()
    if case["expect_token"]:
        assert "accessToken" in data
    else:
        assert "accessToken" not in data
