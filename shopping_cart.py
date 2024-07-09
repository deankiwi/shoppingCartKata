from typing import List
from product import Product


class ShoppingCart:
    """
    A class to represent a shopping cart.
    
    Attributes:
        products (dict): A dictionary of products available for purchase,
                         keyed by product code.
    
    Methods:
        calculate_subtotal(items: List[dict]) -> int:
            Calculates the subtotal of the cart based on the unit prices and special prices.
    """
    
    def __init__(self, products: List[Product]) -> None:
        """
        Initializes the ShoppingCart with a list of products.
        
        Args:
            products (List[Product]): A list of Product objects available for purchase.
        """
        self.products = {product.code: product for product in products}
    
    def calculate_subtotal(self, items: List[dict]) -> int:
        """
        Calculates the subtotal of the cart based on the unit prices and special prices.
        
        Args:
            items (List[dict]): A list of dictionaries where each dictionary represents
                                an item with 'code' and 'quantity' keys.
                                Example: [{'code': 'A', 'quantity': 3}, {'code': 'B', 'quantity': 2}]
        
        Returns:
            int: The total price of the items in the cart considering any special prices.
        
        Raises:
            KeyError: If any item code in the list does not exist in the products dictionary.
        """
        total = 0
        for item in items:
            code = item['code']
            quantity = item['quantity']
            product = self.products[code]  # will raise KeyError if code not in products
            if product.special_price:
                special_quantity, special_price = product.special_price
                special_count = quantity // special_quantity
                remainder = quantity % special_quantity
                total += special_count * special_price + remainder * product.unit_price
            else:
                total += quantity * product.unit_price
        return total
