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

'''class Store:
    def __init__(self):
        self.customers[]
        self.products[]
        self.orders[]'''


#start interaction

customer = Customer("John")
while True:
    print("___Amazon Lite___")
    print("1. View Products")
    print("2. Add to cart")
    print("3. View cart")
    print("4. Check Out")
    print("5. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        display_products(products)

    elif choice == "2":
        while True:
            display_products(products)
            pid = int(input("Enter product ID to add to cart: "))
            qty = int(input("Enter quantity: "))
            selected = None

            for p in products:
                if p.product_id == pid:
                    selected = p
                    break

            if selected:
                if selected.stock >= qty:
                    selected.stock -= qty
                    customer.add_to_cart(selected, qty)
                    print("✅ Added to cart.")
                else:
                    print("❌ Not enough stock.")
            else:
                print("❌ Product not found.")

            more = input("Do you want to add another item? (yes/no): ").lower()
            if more != "yes":
                break  # exit this loop and return to main menu
    elif choice == '3':
        customer.view_cart()

    elif choice == '4':
        customer.view_cart()
        confirm = input("Confirm checkout? (yes/no): ").lower()
        if confirm == 'yes':
            print("Order placed successfully! Thank you for shopping.")
            break  # end the program after order
        else:
            print("Checkout cancelled.")

    elif choice == '5':
        print("Thank you! Visit again.")
        break

    else:
        print("Invalid choice. Try again.")























