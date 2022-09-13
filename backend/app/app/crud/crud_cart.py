from app.schemas import Product

from app.schemas.product import Product


class Cart(object):
    """"
    Represents a shopping cart.
    """
    def __init__(self):
        """
        Initialize cart.
        """
        self._cart = {}

    def add(self, product: Product, user_id: str, quantity: int=1, update_quantity: bool=False):
        """
        Add a product to the cart or update its quantity.
        """
        if not user_id:
            raise ValueError("User id required")

        if user_id not in self._cart:
            self._cart[user_id] = dict()
        product_id = str(product.id)
        if product_id not in self._cart[user_id]:
            self._cart[user_id][product_id] = {'quantity': 0,
                                        'price': product.price}
        if update_quantity:
            self._cart[user_id][product_id]['quantity'] = quantity
        else:
            self._cart[user_id][product_id]['quantity'] += quantity


    def remove(self, product_id: str, user_id: str):
        """
        Remove a product from the cart.
        """
        if user_id in self._cart:
            del self._cart[user_id][product_id]



    def items(self, user_id):
        """
        Iterate over items in the cart.
        """
        for item in self._cart[user_id].values():
            yield item

    def item_count(self, user_id):
        """
        Count all items in the cart.
        """
        if user_id in self._cart:
            count = sum(item['quantity'] for item in self._cart[user_id].values())
        else:
            count = 0
        return count


    def is_empty(self, user_id: str):
        """
        Check whether the cart is empty.
        """
        return self.item_count(user_id) == 0

    def get_total_cost(self, user_id):
        """
        Calculate total cost of all items in the cart.
        """
        return sum(item['price'] * item['quantity'] for item in
                   self._cart[user_id].values())

    def clear(self, user_id):
        """
        Remove the cart from the session.
        """
        self._cart[user_id] = {}
        del self._cart[user_id]

    def summary(self, user_id):
        """
        Return a summary.
        """
        is_empty = self.is_empty(user_id)
        return {
            "item_count": self.item_count(user_id) if not is_empty else 0,
            "total_cost": self.get_total_cost(user_id) if not is_empty else 0
        }


cart = Cart()