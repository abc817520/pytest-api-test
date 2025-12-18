from common.request_util import RequestUtil

class CartApi:

    def add_cart(self, user_id, product_id, quantity=1):
        data = {
            "userId": user_id,
            "products": [
                {
                    "id": product_id,
                    "quantity": quantity
                }
            ]
        }
        return RequestUtil.post("/carts/add", json=data)
