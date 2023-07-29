"""
FUNCTIONS.
Functions are a way to encapsulate a block of code that can be reused and called multiple times. 
They allow you to break down your code into smaller, more manageable pieces, improving readability and reusability.

Defining a Function:
We use the def keyword followed by the function name and a pair of parentheses. 
If the function takes parameters, you list them within the parentheses. 
The function block is indented below the function definition.

def hello():
    print("A good afternoon")
"""

def add_numbers(a, b):      # function can return values using the return statement
    return a + b

# Calling a function
print(add_numbers(5, 3))

# Arguments and parameters.
# Parameters.  a and b are parameters
# Arguments. are the values passed into the function call. 5 and 3 are arguments

# Passing a List to a function
numbers1 = [2, 4, 5, 10]

def squares(nums):
    for num in nums:
        print(num**2)

squares(numbers1)

"""
Default Parameters:
You can assign default values to parameters in a function.
If a value is not provided for a parameter, the default value will be used instead.
"""

def welcome(name="there"):
    print("You are welcome, " + name + "!")

welcome()
welcome("Alice")

# Example.2

def make_cup_of_tea(tea_type, sugar=True, milk=False):
    cup = "A cup of " + tea_type + " tea"

    if sugar:
        cup += " with sugar"

    if milk:
        cup += " with milk"

    return cup

# Calling the function with different arguments
print(make_cup_of_tea("black"))
print(make_cup_of_tea("green", milk=True))
print(make_cup_of_tea("herbal", sugar=False, milk=True))

"""
Variable Number of Arguments:
Functions can accept a variable number of arguments by using *args or **kwargs in the parameter list. 
*args allows you to pass multiple positional arguments, while **kwargs allows you to pass multiple keyword arguments.
"""

def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

result = sum_numbers(1, 2, 3, 4)
print(result)

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key + ": " + value)


print_info(name="Alice", age="25", country="USA")

"""
Function Scope and Variable Visibility:

Local Variables: Variables defined inside a function are local to that function and can only be accessed within the function.
Global Variables: Variables defined outside of any function, at the module level, are global variables and can be accessed from any part of the code.
Global Keyword: The global keyword allows you to modify a global variable from within a function.
Nonlocal Keyword: The nonlocal keyword allows you to modify a variable from an outer (enclosing) function within a nested function.
"""

def outer_function():
    outer_var = "I'm local to outer_function"

    def inner_function():
        nonlocal outer_var
        inner_var = "I'm local to inner_function"
        print(inner_var)
        print(outer_var)

    inner_function()
    print(outer_var)
    # print(inner_var)  # This will cause an error since inner_var is not visible outside of inner_function

outer_function()
# print(outer_var)  # This will cause an error since outer_var is not visible outside of outer_function


# MODULES.
"""
Modules are files containing Python code that define functions, classes, and variables that can be used in other Python programs. 
They provide a way to organize and reuse code by breaking it into separate files. 
Modules can be built-in modules that come with Python or custom modules created by users.

Importing Modules:
To use code from a module in your program, you need to import it. The import keyword is used to import a module into your Python script.
Once imported, you can access the functions, classes, and variables defined in the module.
"""
# area of a circle
# .. lets say i create a .py file called sil_module and i have a greet function inside it
import sil_module
import math

radius = 5
area = math.pi * math.pow(radius, 2)
print(area)

# Importing Specific Objects:
# If you only need specific objects from a module, you can import them individually using the from keyword.
from math import pi, pow

radius = 10
area = pi * pow(radius, 2)
print(area)

# Importing with an Alias:
# You can assign an alias to a module when importing it, using the as keyword.
# This allows you to use a shorter or more descriptive name when referencing the module.
import math as m

radius = 15
area = m.pi * m.pow(radius, 2)
print(area)  

# Importing Multiple Modules:
# You can import multiple modules at once by separating them with commas.
import math, random

radius = 20
area = math.pi * math.pow(radius, 2)
print(area)

random_number = random.randint(1, 100)
print(random_number)

# Creating Custom Modules:
# You can create your own custom modules by creating a Python file and defining functions, classes, or variables within it.
# Once created, you can import and use your custom module in other Python scripts.
# sil_module.greet("Silver")   # this is the greet function in the sil_module.py file.

from math import sqrt, factorial

print(sqrt(16))
print(factorial(5))

import sil_module
print(sil_module.product(8, 4))

# INPUT AND OUTPUT
# checking user input
ans = int(input("What is 5 + 5? "))
if ans == 10:
    print("You got it right!")

# Example.2
age = int(input("Enter your age: "))
if age < 0:
    print("Invalid age!")
elif age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")

# Example.3  Multiple inputs using split():
values = input("Enter a list of values (separated by space): ")
numbers = values.split()
sum = 0
for num in numbers:
    sum += int(num)
print("The sum is:", sum)

# Example.4
# s,r,w = map(int, input("Enter the values: ").split())
# print("The values are: ", end = " ")
# print(s,w)

# Example.5  Capture input from tuple
# d = (2,4,6,8)
# print("Current tuple")
# print(d)

# E = list(d)
# E.append(int(input("Enter a value: ")))
# d = tuple(E)

# print("Updated tuple")
# print(d)


# sil_list = list(map(int, input("Enter the values: ").split()))
# print(sil_list)

# mySet = set(map(int, input("Enter the values: ").split()))
# print(mySet)


"""
EXCEPTION HANDLING
Exception handling is a way to handle and manage errors or exceptional conditions that may occur during the execution of a program. 
It allows you to gracefully handle errors and prevent your program from abruptly terminating.
Python provides a try-except block for handling exceptions.
try:
    # Code that may raise an exception
except ExceptionType1:
    # Code to handle ExceptionType1
except ExceptionType2:
    # Code to handle ExceptionType2
else:
    # Code to execute if no exceptions were raised
finally:
    # Code that will always execute, regardless of whether an exception occurred or not

Types of exceptions
1. Exception: The base class for all built-in exceptions. It can be used to catch any exception that occurs in your code.
2. TypeError: Raised when an operation or function is applied to an object of inappropriate type.  ( "23" + 3 )
3. ValueError: Raised when a function receives an argument of the correct type but an invalid value.   (int("ab"))
4. NameError: Raised when a local or global name is not found.  print("undefined_variable")
This typically occurs when you try to access a variable or function that hasn't been defined.
5. IndexError: Raised when a sequence subscript (index) is out of range. 
It occurs when you try to access an element with an invalid index in a sequence like a list or string.
6. KeyError: Raised when a dictionary key is not found.
7. FileNotFoundError: Raised when a file or directory is requested but cannot be found.
8. IOError: Raised when an input/output operation fails.
9. ZeroDivisionError: Raised when division or modulo operation is performed with zero as the divisor.
10. AttributeError: Raised when an attribute reference or assignment fails.
11. ImportError: Raised when a module or package is not found or fails to be imported.
12. PermissionError: Raised when a program doesn't have the necessary permissions to perform a specific operation on a file or directory.
13. KeyboardInterrupt: Raised when the user interrupts the execution of the program, typically by pressing Ctrl+C.
"""
try:
    n = 4/0
    print("The result is:", n)
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Always executed.")

# Example.2
try:
    my_list = [1, 2, 3]
    print(my_list[4])
except IndexError as e:
    print("An IndexError occurred:", str(e))

# Example.3
try:
    import non_existent_module
except ImportError:
    print("Error: Module not found.")

# Example.4
try:
    num = 42
    print(num.length)        # tries to access the attribute length of an integer, which doesn't exist.
except AttributeError:
    print("Error: 'int' object has no attribute 'length'.") 

# Example.5
try:
    file = open("nonexistent_file.txt", "r")
    content = file.read()
    print("File content:", content)
except FileNotFoundError:
    print("Error: File not found.")

# Custom Exceptions.
class CustomError(Exception):
    pass

try:
    num = int(input("Enter a number: "))
    if num < 0:
        raise CustomError("Negative numbers not allowed.")
    else:
        print("Number:", num)
except CustomError as ce:
    print("Error:", str(ce))


""" 
FILE HANDLING 
Process of working with files on a computer system.
"""
# Opening a File : open() function.
file = open("data.txt", "r")    # Open the file in read mode. File pointer is at the beginning of the file.
file = open("output.txt", "w")  # Open the file in write mode. Truncates the file if it exists, or creates a new file.
file = open("output.txt", "a")  # Open the file in append mode. File pointer is at the end of the file, and new data is appended.
file = open("output.txt", "x")  # Exclusive creation mode. Creates a new file, but raises an error if it already exists.

# Reading from a File 
# read() .. reads the entire file content as a string.
# readline() .. reads one line at a time.
# readlines() .. reads all lines into a list.

# Writing to a File
# write() method allows you to write a string to the file.
# writelines() takes a list of strings and writes them to the file.

# Closing a File : close() function.


file = open("data.txt", "r")
content = file.read()
# print(content)
file.close()

file = open("output.txt", "w")
file.write("Hello, World!\n")
file.close()

file = open("output.txt", "a")
file.write("This is a new line.\n")
file.close()

# Handling exceptions in files. 
try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)

except FileNotFoundError:
    print("File not found.")

except PermissionError:
    print("Permission denied.")

finally:
    file.close()

# Using with statement.
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Example.2
try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: File not found.")
except ValueError:
    print("Error: Invalid content in the file.")
except Exception as e:
    print("Error:", str(e))
finally:
    if file:
        file.close()


""" 
DIRECTORY HANDLING.
Involves working with directories (folders) in the file system. 
Python provides modules like os and shutil that offer various functions and methods to perform directory-related operations. 
"""
import os, shutil

def create_directory(directory_path):
    os.mkdir(directory_path)
    print(f"Directory '{directory_path}' created successfully.")

def remove_directory(directory_path):
    os.rmdir(directory_path)
    print(f"Directory '{directory_path}' removed successfully.")

def list_directory(directory_path):
    content = os.listdir(directory_path)
    print(f"Contents of directory '{directory_path}':")
    for file in content:
        print(file)

def check_directory_exists(directory_path):
    if os.path.exists(directory_path):
        print(f"Directory '{directory_path}' exists.")
    else:
        print(f"Directory '{directory_path}' does not exist.")

def delete_directory(directory_path):
    try:
        shutil.rmtree(directory_path)
        print(f"Directory '{directory_path}' deleted successfully.")
    except FileNotFoundError:
        print(f"Directory '{directory_path}' does not exist.")
    except OSError as e:
        print(f"Error occurred while deleting directory '{directory_path}': {str(e)}")

def CWD():
    cwd = os.getcwd()
    print("Current directory:", cwd)

if __name__ == "__main__":
    # Call the functions
    directory_path = "folder2" 
    non_empty_dire = "folder1"
    CWD()
    # create_directory(directory_path)
    # check_directory_exists(directory_path)
    # list_directory(directory_path)
    # remove_directory(directory_path)  # .. only empty directories
    # delete_directory(non_empty_dire)
    