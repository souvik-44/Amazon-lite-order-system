"""
Amazon Lite - A basic online ordering system
"""
from Store import Product
from datetime import datetime
import uuid

class Payment:
    def __init__(self, amount, payment_method):
        self.amount = amount
        self.payment_method = payment_method
        self.status = "pending"
        self.payment_id = str(uuid.uuid4())
        self.timestamp = datetime.now()

    def process_payment(self):
        # Simulate payment processing
        self.status = "completed"
        return True

class Cart:
    def __init__(self):
        self.items = []
        self.total = 0

    def add_item(self, product, quantity):
        if quantity > product.stock:
            raise ValueError(f"Only {product.stock} units of {product.name} available")
        self.items.append({
            'product': product,
            'quantity': quantity
        })
        product.stock -= quantity
        self.total += product.price * quantity

    def remove_item(self, product_id):
        for item in self.items:
            if item['product'].product_id == product_id:
                self.total -= item['product'].price * item['quantity']
                item['product'].stock += item['quantity']
                self.items.remove(item)
                return True
        return False

    def update_quantity(self, product_id, new_quantity):
        for item in self.items:
            if item['product'].product_id == product_id:
                old_quantity = item['quantity']
                if new_quantity > item['product'].stock + old_quantity:
                    raise ValueError(f"Only {item['product'].stock + old_quantity} units available")
                
                item['product'].stock += old_quantity
                item['product'].stock -= new_quantity
                self.total -= item['product'].price * old_quantity
                self.total += item['product'].price * new_quantity
                item['quantity'] = new_quantity
                return True
        return False

    def get_total(self):
        return self.total

class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = Cart()
        self.orders = []

    def add_to_cart(self, product, quantity):
        self.cart.add_item(product, quantity)

    def remove_from_cart(self, product_id):
        return self.cart.remove_item(product_id)

    def update_cart_quantity(self, product_id, new_quantity):
        return self.cart.update_quantity(product_id, new_quantity)

    def view_cart(self):
        if not self.cart.items:
            return "Cart is empty"
        cart_items = []
        for item in self.cart.items:
            cart_items.append(f"{item['product'].name} x {item['quantity']} = ${item['product'].price * item['quantity']}")
        return "\n".join(cart_items) + f"\nTotal: ${self.cart.get_total()}"

class Order:
    def __init__(self, customer):
        self.order_id = str(uuid.uuid4())
        self.customer = customer
        self.items = customer.cart.items
        self.total = customer.cart.get_total()
        self.payment = None
        self.status = "pending"
        self.timestamp = datetime.now()

    def process_payment(self, payment_method):
        self.payment = Payment(self.total, payment_method)
        if self.payment.process_payment():
            self.status = "completed"
            return True
        return False

def display_products(products):
    print("\nAvailable Products:")
    for product in products:
        print(f"{product}")

# Interactive menu
def main():
    print("Welcome to Amazon Lite!")
    customer_name = input("Please enter your name: ")
    customer = Customer(customer_name)

    while True:
        print("\n1. View Products\n2. Add to Cart\n3. View Cart\n4. Update Cart\n5. Remove from Cart\n6. Place Order\n7. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            display_products(products)
        elif choice == "2":
            while True:
                display_products(products)
                product_id = input("Enter product ID to add (or 'done' to finish): ")
                
                if product_id.lower() == 'done':
                    break
                    
                try:
                    product_id = int(product_id)
                    quantity = int(input("Enter quantity: "))
                    product = next(p for p in products if p.product_id == product_id)
                    customer.add_to_cart(product, quantity)
                    print(f"Added {quantity} {product.name}(s) to cart!")
                    
                    # Ask if user wants to add more
                    add_more = input("Add another item? (yes/no): ").lower()
                    if add_more != 'yes':
                        break
                        
                except StopIteration:
                    print("Product not found!")
                except ValueError as e:
                    print(e)
        elif choice == "3":
            print("\nCart Contents:")
            print(customer.view_cart())
        elif choice == "4":
            product_id = int(input("Enter product ID to update: "))
            new_quantity = int(input("Enter new quantity: "))
            try:
                if customer.update_cart_quantity(product_id, new_quantity):
                    print("Cart updated successfully!")
                else:
                    print("Product not found in cart!")
            except ValueError as e:
                print(e)
        elif choice == "5":
            product_id = int(input("Enter product ID to remove: "))
            if customer.remove_from_cart(product_id):
                print("Item removed from cart!")
            else:
                print("Product not found in cart!")
        elif choice == "6":
            if not customer.cart.items:
                print("Cart is empty!")
                continue
            
            order = Order(customer)
            print(f"Total amount: ${order.total}")
            payment_method = input("Enter payment method (credit/debit): ")
            
            if order.process_payment(payment_method):
                print("Order placed successfully!")
                customer.orders.append(order)
                customer.cart = Cart()  # Clear cart after successful order
            else:
                print("Payment processing failed!")
        elif choice == "7":
            print("Thank you for shopping!")
            break
        else:
            print("Invalid choice!")

# Store inventory
products = [
    Product(1, "Laptop", 1000,5),
    Product(2,"Television",500,7),
    Product(3,"Air Condition",700,10),
    Product(4,"XBOX",600,12),
    Product(5,"Microwave",300,9)
]

if __name__ == "__main__":
    main()


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

























