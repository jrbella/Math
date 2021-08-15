
# Raise to the power of
def powa(number, power):
    return number ** power

# simplify an expression
# expressions should be entered as a string array
def simplify_expression(strArr):
    # iterate over the expression
    for value in strArr:
        # iterate over each character in the expression
        for char in value:
            # evaluate if it is a number, operator or letter
            print("test Param")
# helper function to find an operator

def is_operator(value):
    operators = [
        '+',
        '-',
        '/',
        '*'
    ]
    if value in operators:
        return True
    else:
        return False

