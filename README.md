# Shopping Cart Kata

This project implements a simple checkout system with special pricing rules.

## Classes

- `Product`: Represents a product with a code, unit price, and optional special price.
- `ShoppingCart`: Manages the products in the cart and calculates the subtotal based on the unit prices and special prices.

## Prerequisites
- [Python 3.12](https://www.python.org/)
- [Git](https://git-scm.com/)

## Usage

1. **Clone the repository**:
    ```sh
    git clone https://github.com/deankiwi/shoppingCartKata.git
    cd shopping-cart-kata
    ```

2. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the tests**:
    ```sh
    python3 -m pytest
    ```

4. **Example Usage**:
    ```python
    from product import Product
    from shopping_cart import ShoppingCart

    # Define products
    product_A = Product("A", 50, (3, 140))
    product_B = Product("B", 35, (2, 60))
    product_C = Product("C", 25)
    product_D = Product("D", 12)

    products = [product_A, product_B, product_C, product_D]

    # Create shopping cart
    cart = ShoppingCart(products)

    # Define items to be added to the cart
    items = [
        {"code": "A", "quantity": 3},
        {"code": "B", "quantity": 3},
        {"code": "C", "quantity": 1},
        {"code": "D", "quantity": 2},
    ]

    # Calculate subtotal
    subtotal = cart.calculate_subtotal(items)
    print(f"Subtotal: {subtotal}")
    ```

