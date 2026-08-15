# Personal Order System

subtotal = 0
discounted = 0
final_price = 0
grand_total = 0
isMember = ""

receipt = ""

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
print()

product_quantity = int(input("How many products are you planning to purchase?: "))

while True:
    isMember = input("Do you have a membership? (Y/N): ").upper()

    if isMember == "Y" or isMember == "N":
        break
    else:
        print("Invalid input, try again!")

print()

for i in range(product_quantity):
    product_name = input(f"Product #{i + 1}: ")
    price = int(input("Price: "))
    quantity = int(input("Quantity: "))
    print()

    subtotal = price * quantity

    if isMember == "Y" and subtotal >= 1000:
        discounted = subtotal * 0.30

    elif isMember == "Y" and subtotal >= 500:
        discounted = subtotal * 0.20

    elif subtotal >= 1000:
        discounted = subtotal * 0.20

    elif subtotal >= 500:
        discounted = subtotal * 0.10

    else:
        discounted = 0

    final_price = subtotal - discounted
    grand_total += final_price

    receipt += f"""
Product #{i + 1}: {product_name}
Price: {price}
Quantity: {quantity}\n
Subtotal: {subtotal}
Discount: {discounted}
Final Price: {final_price}
"""

print()
print("========== RECEIPT ==========")
print(f"Customer: {user_name.capitalize()}")
print(f"Age: {user_age}")
print(receipt)
print(f"Grand Total: {grand_total}")