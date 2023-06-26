def find_max_sum_subarray(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    # Variables to track the maximum sum and its corresponding subarray
    max_sum = float('-inf')
    left = 0
    right = 0
    top = 0
    bottom = 0

    # Iterate over each column as the left and right boundaries
    for l in range(columns):
        # Initialize an array to track the cumulative sum for each row
        cumulative_sum = [0] * rows

        for r in range(l, columns):
            # Update the cumulative sum for each row
            for i in range(rows):
                cumulative_sum[i] += matrix[i][r]

            # Apply Kadane's algorithm to find the maximum sum subarray in the cumulative sum
            current_sum = 0
            current_top = 0
            current_bottom = -1
            temp_top = 0

            for i in range(rows):
                current_sum += cumulative_sum[i]

                if current_sum < 0:
                    current_sum = 0
                    temp_top = i + 1
                elif current_sum > max_sum:
                    max_sum = current_sum
                    left = l
                    right = r
                    top = temp_top
                    bottom = i

    # Extract the maximum sum subarray from the original matrix
    subarray = []
    for i in range(top, bottom + 1):
        subarray.append(matrix[i][left:right + 1])

    return max_sum, subarray


# Test the function
matrix = [
    [1, 2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6]
]

max_sum, max_subarray = find_max_sum_subarray(matrix)

# Display the maximum sum and the corresponding subarray
print("Maximum Sum:", max_sum)
print("Maximum Sum Subarray:")
for row in max_subarray:
    print(row)
