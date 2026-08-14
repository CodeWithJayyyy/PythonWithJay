import time

secret_number = 75
user_guess = 0



print("---Number Guessing Game ---")

while  secret_number != user_guess:

    user_guess = int(input("Enter a number (1-100): "))

    if user_guess == secret_number:
         time.sleep(2)
         print("Processing.")
         time.sleep(2)
         print("Processing..")
         time.sleep(2)
         print("Processing...")
         time.sleep(2)
         print("Wow you finally got it correct!")
         time.sleep(2)
         print("After all these trial and error you actually won")
         time.sleep(3)
         print("Congrats winning on....")
         time.sleep(2)
         print("Nothing!")
         time.sleep(2)
         print("Thank you for wasting your time!")
         break


    if user_guess <= 10:
        print("Are you even trying?")
        time.sleep(0.5)
        print("Your too far!")
        time.sleep(0.3)
        print("Try Again.")

    elif user_guess <= 40:
        print("Hmm, not bad but not good i guess?")
        time.sleep(0.5)
        print("Keep trying bud")

    elif user_guess <= 65:
        print("I think your getting better at this")
        time.sleep(0.5)
        print("Try again")

    elif user_guess <= 74:
        time.sleep(2)
        print("Wow")
        time.sleep(2)
        print("You actually got it")
        time.sleep(2)
        print("WRONG!")
        print("keep trying you might actually win")

    else:
        print("I think you went above")
        print("Not bad but try again!")
              
       