import tkinter as tk



class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

products = [
    Product(1, "Laptop", 1000, 5),
    Product(2, "Television", 500, 7),
    Product(3, "Air Conditioner", 700, 10),
    Product(4, "XBOX", 600, 12),
    Product(5, "Microwave", 300, 9)
]

cart = []

def add_to_cart(product):
    cart.append({'product': product, 'quantity': 1})
    status_label.config(text=f"{product.name} added to cart!", fg="green")

def view_cart():
    cart_window = tk.Toplevel(root)
    cart_window.title("🛒 Your Cart")
    cart_window.configure(bg="white")
    total = 0
    for item in cart:
        p = item["product"]
        q = item["quantity"]
        subtotal = p.price * q
        total += subtotal
        label = tk.Label(cart_window, text=f"{p.name} x {q} = ₹{subtotal}", bg="white", font=("Arial", 12))
        label.pack(anchor="w", padx=10)
    total_label = tk.Label(cart_window, text=f"Total: ₹{total}", bg="white", font=("Arial", 12, "bold"))
    total_label.pack(pady=10)

# Setup window
root = tk.Tk()
root.title("Amazon Lite - GUI Version")
root.configure(bg="white")

# Dynamically show product name + Add button
for i, product in enumerate(products):
    # Label for product
    label = tk.Label(root,
                     text=f"{product.name} - ₹{product.price} (Stock: {product.stock})",
                     font=("Arial", 12),
                     bg="white",
                     fg="black",
                     anchor="w",
                     justify="left")
    label.grid(row=i, column=0, sticky="w", padx=10, pady=5)

    # Button to add
    button = tk.Button(root, text="Add", command=lambda p=product: add_to_cart(p))
    button.grid(row=i, column=1, padx=10)

# Status message
status_label = tk.Label(root, text="", font=("Arial", 11), bg="white", fg="black")
status_label.grid(row=len(products), column=0, columnspan=2)

# View Cart Button
view_btn = tk.Button(root, text="🛒 View Cart", command=view_cart)
view_btn.grid(row=len(products)+1, column=0, columnspan=2, pady=10)

root.mainloop()