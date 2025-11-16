class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        """Add item to the cart"""
        try:
            price = float(price)
            if price < 0:
                print("❌ Price cannot be negative.")
                return
            if name in self.items:
                self.items[name] += price
            else:
                self.items[name] = price
            print(f"✅ {name} added to cart (₹{price:.2f})")
        except ValueError:
            print("❌ Invalid price. Please enter a number.")

    def remove_item(self, name):
        """Remove item if it exists"""
        if name in self.items:
            del self.items[name]
            print(f"🗑️ {name} removed from cart.")
        else:
            print("⚠️ Item not found in cart.")

    def total_cost(self):
        """Return total cart value"""
        return round(sum(self.items.values()), 2)

    def check_item(self, name):
        """Check if an item exists in the cart"""
        if name in self.items:
            print(f"✅ {name} is in the cart (₹{self.items[name]:.2f}).")
        else:
            print(f"❌ {name} is not in the cart.")

    def show_cart(self):
        """Display all items"""
        if not self.items:
            print("🛒 Cart is empty.")
        else:
            print("\n🛍️ Items in your cart:")
            for name, price in self.items.items():
                print(f" - {name}: ₹{price:.2f}")
            print(f"💰 Total cost: ₹{self.total_cost():.2f}\n")


# ======== USER INTERFACE ========

cart = ShoppingCart()

print("🛒 Welcome to the Python Shopping Cart!")
print("Type 'quit' anytime to exit.\n")

while True:
    print("\nChoose an option:")
    print("1️⃣ Add item")
    print("2️⃣ Remove item")
    print("3️⃣ Show cart")
    print("4️⃣ Check if item is included")
    print("5️⃣ Show total cost")
    print("6️⃣ Quit")

    choice = input("👉 Enter choice (1-6 or 'quit'): ").strip().lower()

    if choice in {"6", "quit", "exit"}:
        print("\n👋 Thank you for shopping! Exiting now...")
        break

    elif choice == "1":
        name = input("Enter item name: ").strip()
        if name.lower() in {"quit", "exit"}:
            print("👋 Exiting now...")
            break
        price = input("Enter item price: ").strip()
        if price.lower() in {"quit", "exit"}:
            print("👋 Exiting now...")
            break
        cart.add_item(name, price)

    elif choice == "2":
        name = input("Enter item name to remove: ").strip()
        if name.lower() in {"quit", "exit"}:
            print("👋 Exiting now...")
            break
        cart.remove_item(name)

    elif choice == "3":
        cart.show_cart()

    elif choice == "4":
        name = input("Enter item name to check: ").strip()
        if name.lower() in {"quit", "exit"}:
            print("👋 Exiting now...")
            break
        cart.check_item(name)

    elif choice == "5":
        print(f"💰 Total cart cost: ₹{cart.total_cost():.2f}")

    else:
        print("❌ Invalid choice. Please select between 1 and 6 or type 'quit'.")


