# This is a single-line comment

x = 5  # This comment explains the purpose of the variable assignment

'''
This is a multiline comment in Python.
It can span multiple lines without the need for the # symbol.
'''

"""
Another way to create a multiline comment.
Use triple double-quotes for this style.
"""

# Some code here...
x = 5
y = 10
result = x + y

print(result)

'''
You can use multiline comments to provide detailed explanations
or temporarily "comment out" blocks of code.
'''

def calculate_sum(a, b):
    """
    Calculate the sum of two numbers.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The sum of the two numbers.
    """
    return a + b

print(calculate_sum(55, 10))
print(calculate_sum.__doc__)
