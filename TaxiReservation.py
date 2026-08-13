import time
#Taxi Reservation System.

#Variable initalization for if else to work
user_name = ""
user_destination = ""
user_age = 0
regular_fare = 100.00

#Welcome user or welcome page
print("""Hello, welcome to Tazi, a simple transportation 
system where you can reserve or request your own 
Tazi and travel safely to your destination.""")

#delay input for console readability
time.sleep(1)
#add space for the user selection, good for console readability and no overlapping
print()

print(""" Please select an option:
1. Reserve a tazi
2. Call a tazi
""")
#user choice and also for user input alignment practice.
user_choice = int(input("Please choose an option from (1-2): "))

#Choice 1 Reservation input and user info gathering.
if user_choice == 1:
    print("Please fill out this information below:")
    print()
    user_name = input("Please enter your name: ")
    user_destination = input("Please enter your destination: ")
    user_age = int(input("Please enter your age: "))

#choice 2 call a tazi(uber) + info gathering for discount eligibility.
elif user_choice == 2:
    time.sleep(1)
    print("Locating nearest tazi...")
    time.sleep(0.5)
    user_destination = input("Please enter your destination: ")
    user_age = int(input("Please enter your age: "))
    print("Please wait for a couple min... your tazi will arrive shortly! Thank you so much for using this system!")

#Discount(20%) eligibility for Students and seniors. (i can still add more discounts in the future :).  )
if user_age <= 21 or user_age >= 60:
    discount = regular_fare * 0.2
    discounted_fare = regular_fare - discount
    total = discounted_fare
    print("You're qualified for the discount, Congrats!")
    print(f"Fare cost is: ₱{discounted_fare}")

#if user did not qualify or is not eligible for the fare discount, user gets regular fare.
else:
    print("Sorry but you're not eligible for a discount.")
    time.sleep(0.5)
    print(f"Fare cost is: ₱{regular_fare}")
    total = regular_fare

#User receipt
time.sleep(2)
print()
print(f"---Tazi Reservation---")
print(f"Name: {user_name}")
print(f"Age: {user_age}")
print(f"Destination: {user_destination}")
print(f"Total cost: ₱{total}")
print()
print(f"""Hello {user_name}, thank you for using the system.
Have a nice trip.""")