def find_second_largest(numbers):
    if len(numbers) < 2:
        return None

    largest = float('-inf')
    second_largest = float('-inf')

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num

    return second_largest


# Test the function
numbers = [5, 9, 1, 3, 7, 2, 8, 4, 6]

second_largest = find_second_largest(numbers)

# Display the second-largest number
if second_largest is not None:
    print("The second-largest number is:", second_largest)
else:
    print("There is no second-largest number in the list.")
