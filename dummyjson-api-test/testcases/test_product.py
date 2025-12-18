import allure
from api.product_api import ProductApi
from common.yaml_util import load_test_data

@allure.feature("商品模块")
@allure.story("获取商品列表")
def test_get_products(login):
    res = ProductApi().list_products()

    assert res.status_code == 200
    assert res.json()["total"] > 0

@allure.story("商品详情-接口依赖")
def test_product_detail(login):
    products = ProductApi().list_products().json()
    product_id = products["products"][0]["id"]

    res = ProductApi().get_product(product_id)
    assert res.status_code == 200
    assert res.json()["id"] == product_id


