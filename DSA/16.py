def find_maximum(a, b, c, d):
    max_value = a

    if b > max_value:
        max_value = b

    if c > max_value:
        max_value = c

    if d > max_value:
        max_value = d

    return max_value


# Test the program
num1 = 10
num2 = 25
num3 = 15
num4 = 20

maximum = find_maximum(num1, num2, num3, num4)
print("The maximum number is:", maximum)
