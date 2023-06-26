def decimal_to_binary(n):
    if n == 0:
        return 0
    else:
        return (n % 2) + 10 * decimal_to_binary(n // 2)


# Test the program
decimal_number = 27

binary_number = decimal_to_binary(decimal_number)

print("Decimal:", decimal_number)
print("Binary:", binary_number)
