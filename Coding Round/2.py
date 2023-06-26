# Program to convert decimal number to binary

# Function to convert decimal to binary
def decimal_to_binary(decimal):
    binary = ""
    
    # Edge case for decimal 0
    if decimal == 0:
        return "0"
    
    while decimal > 0:
        # Get the remainder when dividing by 2
        remainder = decimal % 2
        
        # Add the remainder to the binary representation
        binary = str(remainder) + binary
        
        # Update the decimal by dividing by 2
        decimal = decimal // 2
    
    return binary

# Get user input for decimal number
decimal_number = int(input("Enter a decimal number: "))

# Convert decimal to binary
binary_number = decimal_to_binary(decimal_number)

# Display the binary representation
print("Binary representation:", binary_number)
