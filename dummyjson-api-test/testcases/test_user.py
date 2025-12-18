import allure
from api.user_api import UserApi
from common.yaml_util import get_config

@allure.feature("用户模块")
@allure.story("获取当前用户信息")
def test_get_user_info(login):
    res = UserApi().get_user_info()

    assert res.status_code == 200
    assert res.json()["username"] == get_config()["username"]
