def find_missing_number(arr):
    n = len(arr) + 1
    total_sum = (n * (n + 1)) // 2  # Sum of all numbers from 1 to n
    array_sum = sum(arr)  # Sum of the given array
    missing_number = total_sum - array_sum
    return missing_number

# Test the function
array = [1, 4, 3, 6, 2, 7, 8]

missing_number = find_missing_number(array)

print("The missing number is:", missing_number)
