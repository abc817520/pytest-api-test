import allure
from api.user_api import UserApi
from api.product_api import ProductApi
from api.cart_api import CartApi

@allure.feature("购物车模块")
@allure.story("添加商品到购物车")
def test_add_cart(login):
    user = UserApi().get_user_info().json()
    products = ProductApi().list_products().json()

    user_id = user["id"]
    product_id = products["products"][0]["id"]

    res = CartApi().add_cart(user_id, product_id)
    assert res.status_code == 201
    assert res.json()["totalProducts"] > 0
