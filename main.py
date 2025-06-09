from app import *

def main():
    print("Amazon Lite CLI is running...")

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

if __name__ == "__main__":
    main()