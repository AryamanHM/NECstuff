# Program to convert ASCII values to a string

# Function to convert ASCII values to a string
def ascii_to_string(ascii_list):
    string = ""
    for ascii_value in ascii_list:
        character = chr(ascii_value)
        string += character
    return string

# Get user input for ASCII values
ascii_values = input("Enter a list of ASCII values separated by spaces: ").split()

# Convert ASCII values to integers
ascii_values = [int(value) for value in ascii_values]

# Convert ASCII values to a string
result_string = ascii_to_string(ascii_values)

# Display the string
print("Output string:", result_string)
