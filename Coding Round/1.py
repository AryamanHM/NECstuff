# Program to display numbers between 32 and 62 that end with 5

# Iterate over the range from 32 to 63 (exclusive)
for number in range(32, 63):
    # Check if the last digit of the number is 5
    if number % 10 == 5:
        print(number)
