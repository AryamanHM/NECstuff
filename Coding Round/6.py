def transpose_matrix(matrix):
    # Get the number of rows and columns in the matrix
    rows = len(matrix)
    columns = len(matrix[0])

    # Create an empty matrix to store the transpose
    transpose = [[0 for _ in range(rows)] for _ in range(columns)]

    # Compute the transpose
    for i in range(rows):
        for j in range(columns):
            transpose[j][i] = matrix[i][j]

    return transpose


# Test the transpose
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed_matrix = transpose_matrix(matrix)

# Display the transposed matrix
for row in transposed_matrix:
    print(row)
