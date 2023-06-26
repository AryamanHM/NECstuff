def find_largest(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        # Find the largest number in the rest of the array
        sub_max = find_largest(arr[1:])

        # Compare the largest number with the first element of the array
        if arr[0] > sub_max:
            return arr[0]
        else:
            return sub_max


# Test the program
array = [10, 5, 8, 20, 3]

largest_number = find_largest(array)

print("Array:", array)
print("Largest number:", largest_number)
