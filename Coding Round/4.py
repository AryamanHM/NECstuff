def rotate_image(matrix):
    # Transpose the matrix
    transposed_matrix = list(zip(*matrix))

    # Reverse each row of the transposed matrix
    rotated_matrix = [list(row[::-1]) for row in transposed_matrix]

    return rotated_matrix


# Test the rotation
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotated_matrix = rotate_image(matrix)

# Display the rotated matrix
for row in rotated_matrix:
    print(row)
