class ApiClient:

    def login(self, username: str, password: str):
        pass

    def get_current_user(self, access_token: str):
        pass

    def get_user_carts(self, user_id: int):
        pass

    def get_cart(self, cart_id: int):
        pass

    def create_cart(self, user_id: int, products: list):
        pass

    def update_cart(self, cart_id: int, products: list):
        pass

    def delete_cart(self, cart_id: int):
        pass