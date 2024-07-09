import pytest
from product import Product
from shopping_cart import ShoppingCart

@pytest.fixture
def cart():
    product_A = Product("A", 50, (3, 140))
    product_B = Product("B", 35, (2, 60))
    product_C = Product("C", 25)
    product_D = Product("D", 12)

    products = [product_A, product_B, product_C, product_D]
    return ShoppingCart(products)

def test_single_item(cart):
    items = [{"code": "A", "quantity": 1}]
    assert cart.calculate_subtotal(items) == 50

def test_no_special_prices(cart):
    items = [
        {"code": "C", "quantity": 4},
        {"code": "D", "quantity": 5},
    ]
    assert cart.calculate_subtotal(items) == 100 + 60

def test_special_prices(cart):
    items = [
        {"code": "A", "quantity": 6},
        {"code": "B", "quantity": 4},
    ]
    assert cart.calculate_subtotal(items) == 280 + 120

def test_multiple_items(cart):
    items = [
        {"code": "A", "quantity": 3},
        {"code": "B", "quantity": 3},
        {"code": "C", "quantity": 1},
        {"code": "D", "quantity": 2},
    ]
    assert cart.calculate_subtotal(items) == 140 + 95 + 25 + 24

def test_key_error(cart):
    items = [{"code": "E", "quantity": 1}]
    with pytest.raises(KeyError):
        cart.calculate_subtotal(items)



