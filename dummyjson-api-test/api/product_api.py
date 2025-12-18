from common.request_util import RequestUtil

class ProductApi:

    def list_products(self):
        return RequestUtil.get("/products")

    def get_product(self, product_id):
        return RequestUtil.get(f"/products/{product_id}")
