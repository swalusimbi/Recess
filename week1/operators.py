# DAY 3 MORNING
# Basic Operators and Expressions
"""
Arithmetic Operators
+ Addition
- Subtraction
* Multiplication
/ Division
// Floor Division .. returns the quotient of a division, rounded down to the nearest integer.
% Modulus
** Exponentiation

Comparison Operators
< Less Than
> Greater Than
<= Less Than or Equal to
>= Greater Than or Equal to
== Equal to
!= Not equal to

Logical Operators  ..   used to combine conditional statements.
Logical AND 'and'
Logical OR 'or'
Logical NOT 'not'

Assignment Operators
Assign value: '='
Add value: '+'
Add and assign value: '+='
Subtract and assign value: '-='
Multiply and assign value: '*='
Divide and assign value: '/='
Modulus and assign value: '%='
Exponentiate and assign value: '**='

Membership Operators
In: 'in' operator: checks if a value exists in a sequence
Not in: 'not in' operator: checks if a value doesnot exist in a sequence

Identity Operators
Is: 'is' operator: returns True if the operands are the same object, and False otherwise.
Is not: 'is not' operator: returns True if the operands are different objects, and False if they refer to the same object.
"""
# Examples on assignment operators
a = 10
b = 3
# Addition
sum = a + b
print("Sum:", sum)

# Subtraction
difference = a - b
print("Difference:", difference)

# Multiplication
product = a * b
print("Product:", product)

# Division
quotient = a / b
print("Quotient:", quotient)

# Floor division
result = a // b
print(result)  # Output: 3

# Modulo
remainder = a % b
print("Remainder:", remainder)

# Exponentiation
power = a ** b
print("Power:", power)

# Examples on comparison operators
x = 5
y = 10

# Equal to
print(x == y)

# Not equal to
print(x != y)

# Greater than
print(x > y)

# Less than
print(x < y)

# Greater than or equal to
print(x >= y)

# Less than or equal to
print(x <= y)

# Examples on logical operators
r = 5
s = 10
t = 3

# and operator
print(r < s and s < t)

# or operator
print(r < s or s < t)

# not operator
print(not (r < s))

# Examples on assignment operators
n = 5
m = 10

# Addition assignment
n += 3
print(n)

# Subtraction assignment
m -= 2
print(m)

# Multiplication assignment
n *= 2
print(n)

# Division assignment
m /= 4
print(m)

# Modulo assignment
n %= 3
print(n)

# Exponentiation assignment
m **= 2
print(m)

# Example on membership operators
fruits = ["apple", "banana", "orange"]
print("apple" in fruits)
print("grape" in fruits)

print("grape" not in fruits)

# using the 'in' operator within an if statement'
word = "Baseball"
if "b" in word:
    print("{} contains the character b".format(word))

# using the 'not in' operator within an if statement
sport = "Golf"
if "b" not in sport:
    print("{} does not contain the character b".format(sport))

#  Example on identity operators
x = [1, 2, 3]
y = [1, 2, 3]
z = x

# is operator
print(x is y)     # False
print(x is z)     # True

# is not operator
print(x is not y)  # True
print(x is not z)  # False

"""
# Bitwise operators: used to perform operations on individual bits of integer values.

Bitwise AND: &
Performs a bitwise AND operation on the binary representation of two integers.
Sets each bit to 1 if both corresponding bits are 1; otherwise, sets it to 0.

Bitwise OR: |
Performs a bitwise OR operation on the binary representation of two integers.
Sets each bit to 1 if at least one of the corresponding bits is 1.

Bitwise XOR: ^
Performs a bitwise XOR (exclusive OR) operation on the binary representation of two integers.
Sets each bit to 1 if only one of the corresponding bits is 1; otherwise, sets it to 0.

Bitwise NOT: ~
Performs a bitwise NOT operation on the binary representation of an integer.
Flips the bits, changing 0 to 1 and 1 to 0.

Bitwise left shift: <<
Shifts the bits of an integer to the left by a specified number of positions.
Fills the vacant bits on the right with zeroes.

Bitwise right shift: >>
Shifts the bits of an integer to the right by a specified number of positions.
Fills the vacant bits on the left with the sign bit (0 for non-negative numbers, 1 for negative numbers).
"""
# Example on bitwise operators
x = 10   # Binary: 1010
y = 6    # Binary: 0110

# Bitwise AND
result_and = x & y
print(result_and)  # Output: 2 (Binary: 0010)

# Bitwise OR
result_or = x | y
print(result_or)   # Output: 14 (Binary: 1110)

# Bitwise XOR
result_xor = x ^ y
print(result_xor)  # Output: 12 (Binary: 1100)

# Bitwise NOT
result_not_x = ~x
print(result_not_x)  # Output: -11 (Binary: -1011)

# Bitwise left shift
result_left_shift = x << 2
print(result_left_shift)  # Output: 40 (Binary: 101000)

# Bitwise right shift
result_right_shift = y >> 1
print(result_right_shift)  # Output: 3 (Binary: 0011)

# Example
# Create a calculator program to add, subtract, multiply, and divide


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def main():
    print("Silver's basic calculator.")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, *, /): ")

    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)
    else:
        print("Invalid operator.")
        return

    print("The result is", result)


if __name__ == '__main__':
    main()

print("*" * 50)