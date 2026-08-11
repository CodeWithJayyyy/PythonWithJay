
option1 = "Pizza"
option2 = "Burger"
option3 = "Fries"

price1 = 18
price2 = 12
price3 = 4

quantity = 0

total = 0

print("Hello what would you like to order? ")
print()
print(f"""Here are the options :
      [1] {option1}
      [2] {option2}
      [3] {option3}
      """)

user_input = int(input("Choose an option 1-3: "))
if user_input == 1:
    print(f"You ordered {option1}")

elif user_input == 2:
    print(f"You ordered {option2}")

elif user_input == 3:
    print(f"You ordered {option3}")

else:
    print("Please try again!")

quantity = int(input("How many would you like? "))

if user_input == 1:
    total = quantity * price1

elif user_input == 2:
    total = quantity * price2

elif user_input == 3:
    total = quantity * price3

else:
 print("NO!")

 print()
print(f"The total amount is {total}₱ ")
