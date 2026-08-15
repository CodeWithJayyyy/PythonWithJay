#For loop exercise
even_sum = 0
odd_sum = 0

odd_count = 0
even_count = 0

print("--- Number Analyzer ---")
print()

numbers = int(input("Enter a number you want to iterate: "))

print("Numbers: ")
for i in range(1,numbers + 1):
    print(i)

print()
print("Even numbers: ")
for even_numbers in range(1,numbers + 1):
    if even_numbers %2 == 0:
        even_sum += even_numbers
        even_count += 1
        print(even_numbers)

print()
print("Odd Numbers: ")
for odd_numbers in range(1,numbers + 1):
    if odd_numbers %2 == 1:
        odd_sum += odd_numbers
        odd_count += 1
        print(odd_numbers)

print()
print(f"Total even numbers: {even_count}")
print(f"Total odd numbers: {odd_count}")   

print()
print(f"Total sum of even numbers: {even_sum}")
print(f"Total sum of odd numbers: {odd_sum}")

