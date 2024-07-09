from typing import Optional, Tuple


class Product:
    """
    A class to represent a product.
    
    Attributes:
        code (str): The item code.
        unit_price (int): The unit price of the product.
        special_price (Optional[Tuple[int, int]]): A tuple containing the special quantity (int) and price (int) (optional).
    """
    def __init__(self, code: str, unit_price: int, special_price: Optional[Tuple[int, int]] = None) -> None:
        self.code = code
        self.unit_price = unit_price
        self.special_price = special_price
