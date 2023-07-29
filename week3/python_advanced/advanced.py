# Advanced topics in python.
"""
Regular Expressions
Generators and Iterators
Decorators
Context managers
Multithreading and multiprocessing

# Regular Expressions 
\d: Matches any digit from 0 to 9. It is equivalent to the character class [0-9].
\w: Matches any alphanumeric character (letter or digit) and underscore. It is equivalent to the character class [a-zA-Z0-9_].
\s: Matches any whitespace character, including spaces, tabs, and line breaks.
. : Matches any character except a newline character.
* : Matches zero or more occurrences of the preceding element. For example, a* matches zero or more "a" characters.
+ : Matches one or more occurrences of the preceding element. For example, a+ matches one or more "a" characters.
? : Matches zero or one occurrence of the preceding element. For example, colou?r matches both "color" and "colour".
[] : Defines a character class, which matches any single character within the brackets. For example, [aeiou] matches any vowel.
[^] : Negates a character class, matching any character not within the brackets. For example, [^0-9] matches any non-digit character.
^ : Matches the start of a line or string.
$ : Matches the end of a line or string.
[] : Defines a character class, which matches any single character within the brackets. For example, [aeiou] matches any vowel.
[^] : Negates a character class, matching any character not within the brackets. For example, [^0-9] matches any non-digit character.
\b: Matches a word boundary, where a word character is followed or preceded by a non-word character. 
 # For example, \bword\b matches the whole word "word" but not "words" or "wording".

"""

# Matching and Searching
# regex  re.match(), re.search(), re.findall()

# Example.1  Demonstrating regex | match first word, match group word, match all numbers
import re

text = "Hello, this is Silver. I am in year 3 of Software engineering, heading to year 4."

# Match first word
match = re.search(r"^\w+", text)

if match:
    print(match.group())

# Match all numbers
matches = re.findall(r"\d+", text)
print("num_list: ",matches)

# Example:2  Validate email format or email address
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    if re.match(pattern, email):
        return True
    else:
        return False

email = "wal@gmcom"
print(validate_email(email))

email2 = "sil@gmail.com"
print(validate_email(email2))

# Assignment.   Validate a password.
import re

def validate_password(password):
    # Check length (at least 8 characters)
    if len(password) < 8:
        return False
    
    # Check for at least one uppercase letter, one lowercase letter, one digit, and one special character
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    
    # All checks passed
    return True

# Prompt the user to enter a password
password = input("Enter a password (should include atleast 8 characters, an upper-case letter, lower-case letter and a number): ")

# Validate the password
is_valid = validate_password(password)
if is_valid:
    print("Password is valid.")
else:
    print("Password is invalid.")


# Generators and iterators
# Generator functions use the yield keyword to define the values of the sequence.
# __iter__() and __next__(). Iterators provide a way to access elements one by one from a collection or sequence.

# Example of an iterator
my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)

print(next(my_iter))  # 1
print(next(my_iter))  # 2
print(next(my_iter))  # 3

print("*" * 40)

# Example of an generator
def factorial(n):
    if n == 0:
        yield 1
    else:
        yield n * next(factorial(n - 1))

# Calculate and print factorials of numbers 1 to 10
for num in range(1, 11):
    result = next(factorial(num))
    print(f"The factorial of {num} is: {result}")

print("*" * 40)

# Example.3  Generate function that yields the square of numbers from 1 to 10
def square_generator():
    for num in range(1, 11):
        yield num ** 2

square_gen = square_generator()

# Print the first 5 squares
for _ in range(5):
    print(next(square_gen))

print("*" * 40)

for square in square_gen:   # Once you iterate over a generator and reach the end,
    print(square)           # subsequent iterations won't yield any more values because the generator has already been exhausted.


# Decorators
# Decorators are a feature in Python that allow you to modify the behavior of functions or classes without directly modifying their source code.
# Decorators use the @decorator_name syntax. 

def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@my_decorator
def greet():
    print("Hello, world!")

# Calling the decorated function
greet()

# Example.2
def deco(fun):
    def wrapper(*args, **kwargs):
        result = fun(*args, **kwargs)
        return result
    return wrapper

@deco
def add(a, b):
    return a + b

print(add(2, 3))

# Example.3
def decorator(cls):
    class ModifiedClass:
        def __init__(self, *args, **kwargs):
            self.instance = cls(*args, **kwargs)
            
        def mtd(self):
            print("Method is modified")

        
    return ModifiedClass

@decorator
class MyClass:
    def mtd(self):
        print("My original method")

obj = MyClass()
obj.mtd()


#  Context managers
""" 
Context managers provide a convenient and reliable way to manage resources, such as files or network connections,
ensuring that they are properly initialized and cleaned up.
Are used with the with statement and follow the "Context Manager Protocol" by implementing the __enter__() and __exit__() methods.

Using the with Statement:
The with statement provides a clean and structured way to work with resources that need to be managed.
It automatically takes care of initializing and cleaning up the resource, even in the presence of exceptions or errors.
"""
# Example of using a context manager with a file
# with open("file.txt", "r") as file:
#     content = file.read()
    
# The file is automatically closed at the end of the block
"""
Implementing a Context Manager:
To create your own context manager, you can define a class that implements the __enter__() and __exit__() methods.
The __enter__() method sets up the resource and returns the resource object, while the __exit__() method handles the cleanup.
"""
class MyContextManager:
    def __enter__(self):         # Initialize the resource
       return resource_object

    def __exit__(self, exc_type, exc_value, traceback):
        # Clean up and release the resource
        pass

# Using the custom context manager
# with MyContextManager() as resource:
    # Perform operations with the resource

""" 
Context Managers Using contextlib:
The contextlib module provides utilities for working with context managers.
The contextlib.contextmanager decorator allows you to define a context manager using a generator function.
This provides a simpler alternative to defining a full class-based context manager.
"""
# Example of a context manager using contextlib
from contextlib import contextmanager

@contextmanager
def my_context_manager():
    resource = initialize_resource()

    try:
        yield resource
    finally:
        # Clean up and release the resource
        cleanup_resource(resource)

# with my_context_manager() as resource:
    

#  Multithreading and multiprocessing