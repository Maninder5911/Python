# Cafe Management System

menu = {
    "coffee": 50,
    "tea": 30,
    "burger": 120,
    "momos": 80,
    "paratha": 60
}

total_bill = 0

print("====== Welcome to Python Cafe ☕ ======")
print("----------- Menu -----------")
for item, price in menu.items():
    print(f"{item.capitalize()} : ₹{price}")

while True:
    choice = input("\nEnter item name (or 'done' to finish): ").lower()

    if choice == "done":
        break

    if choice in menu:
        quantity = int(input(f"Enter quantity of {choice}: "))
        cost = menu[choice] * quantity
        total_bill += cost
        print(f"{choice.capitalize()} x {quantity} = ₹{cost}")
    else:
        print("❌ Item not available")

print("\n============================")
print(f"Total Amount to Pay: ₹{total_bill}")
print("Thank you for visiting our Cafe 😊")
print("=")
