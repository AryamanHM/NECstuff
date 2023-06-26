def infix_to_postfix(expression):
    # Dictionary to store the precedence of operators
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

    # Initialize an empty stack and an empty list to store the postfix expression
    stack = []
    postfix = []

    # Function to check if a token is an operator
    def is_operator(token):
        return token in precedence

    # Function to compare the precedence of two operators
    def has_higher_precedence(op1, op2):
        return precedence[op1] >= precedence[op2]

    # Process each token in the expression
    for token in expression:
        if token.isdigit():
            # If the token is a digit, append it to the postfix expression
            postfix.append(token)
        elif is_operator(token):
            # If the token is an operator, pop operators from the stack to the postfix expression
            # until an operator with lower precedence is encountered or the stack is empty
            while stack and is_operator(stack[-1]) and has_higher_precedence(stack[-1], token):
                postfix.append(stack.pop())
            # Push the current operator to the stack
            stack.append(token)
        elif token == "(":
            # If the token is an opening parenthesis, push it to the stack
            stack.append(token)
        elif token == ")":
            # If the token is a closing parenthesis, pop operators from the stack to the postfix expression
            # until an opening parenthesis is encountered or the stack is empty
            while stack and stack[-1] != "(":
                postfix.append(stack.pop())
            # Pop the opening parenthesis from the stack
            if stack and stack[-1] == "(":
                stack.pop()

    # Pop any remaining operators from the stack to the postfix expression
    while stack:
        postfix.append(stack.pop())

    # Return the postfix expression as a string
    return " ".join(postfix)


# Test the infix to postfix conversion
infix_expression = input("Enter an infix expression: ").split()
postfix_expression = infix_to_postfix(infix_expression)

# Display the postfix expression
print("Postfix expression:", postfix_expression)
