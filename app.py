"""
The program is about creating a ordering system for a amazon like online platform.
    I will require classes to store the customer information and do crud operations
    1. Customer will be able to add items to the cart.
    2. Update and delete the cart.
    3. I will also require a class for customer payments etc. basic level program
"""
from Store import Product

#store inventory
products = [
    Product(1, "Laptop", 1000,5),
    Product(2,"Television",500,7),
    Product(3,"Air Condition",700,10),
    Product(4,"XBOX",600,12),
    Product(5,"Microwave",300,9)
]

#Interactive menu
def display_products(products):
    for product in products:
        print(product)


class Customer:
    def __init__(self,name):
        self.name = name
        self.cart = []

    def add_to_cart(self,product,quantity):
        self.cart.append({'product': product, 'quantity': quantity})

    def view_cart(self):
        if not self.cart:
            print("🛒 Your cart is empty")
        else:
            print("\n🛒 Your Cart:")
            total = 0
            for item in self.cart:
                p = item["product"]
                q = item["quantity"]
                subtotal = p.price * q
                total += subtotal
                print(f"{p.name}  (${p.price}) x {q} = ${subtotal}")
            print("-----------------------------")
            print(f"🧾 Total: ${total}")



class Cart:
    def __init__(self,product,quantity):
        self.product = product
        self.quantity = quantity

class Order:
    def __init__(self,order_id,customer, items):
        self.order_id = order_id
        self.customer = customer
        self.items = items
        self.total = calculate_total()

    def calculate_total(self):
        return sum(item.product.price * item.quantity for item in self.items)

























