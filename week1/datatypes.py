# DAY 2 EVENING
"""
DICTIONARIES.
Dictionaries are a built-in data structure used to store and manipulate collections of key-value pairs. 
Dictionaries are also known as associative arrays or hash maps in other programming languages.
"""

# Creating a dictionary:  enclose comma-separated key-value pairs within curly braces {} or by using the dict() constructor.
# Empty dictionary    # this is not an empty set as one may confuse it to be.
empty = {}
# an empty set is created using the set() constructor only.
print(type(empty))

dictio = {'key1': 'value1', 'key2': 'value2'}

# Using dict() constructor
dictio = dict()
dictio = dict(key1='value1', key2='value2')
"""
Accessing Elements
You can access the values in a dictionary by providing the corresponding key inside square brackets []. 
If the key is not found, it will raise a KeyError. 
Alternatively, you can use the get() method, which returns None (or a specified default value) if the key is not found.
"""
customer = {'fruit': 'Mango', 'price': 250}

print(customer['fruit'])
print(customer.get('price'))
print(customer.get('address'))
print(customer.get('address', 'Unknown'))  # Output: Unknown (default value)

# Getting a list of keys
print(customer.keys())

# Exercise One: using values()
print(customer.values())

# Exercise Two: check if a key exists in a dictionary
print('fruit' in customer)
print('age' in customer)

# Exercise Three: Give an example on how to change dictionary items, how to update
"""
Modifying values:
You can modify the value associated with a specific key by assigning a new value to it.
"""
customer['price'] = 300
print(customer)

# Exercise Four: Give an example on how to add dictionary items, how to remove them
"""
Adding and removing key-value pairs:
To add a new key-value pair, you can simply assign a value to a new key. 
To remove a key-value pair, you can use the del keyword or the pop() method.
"""
person = {"name": "Ellie", "age": 19, "city": "Albion",
          "country": "UK", "hobbies": ["reading", "traveling", "painting"]}

print(person)

person['address'] = 'Makerere'
print(person)

del person['age']
print(person)

person.pop('hobbies')
print(person)

# Exercise Five: Give an example on how to loop through a dictionary and how to nest dictionaries
# Iterating over a dictionary:
# You can iterate over the keys, values, or key-value pairs in a dictionary using the keys(), values(), or items() methods, respectively.
for key in person.keys():
    print(key)

for value in person.values():
    print(value)

for key, value in person.items():
    print(key, value)

# Nesting dictionaries in Python refers to the practice of storing dictionaries as values within another dictionary.
# Creating a nested dictionary
student = {
    "name": "Silver",
    "age": 20,
    "grades": {
        "math": 95,
        "english": 85,
        "science": 92
    }
}

# Accessing nested dictionary values
print(student["name"])
print(student["grades"]["math"])

"""
DICTIONARIES.
Dictionaries are a built-in data structure used to store and manipulate collections of key-value pairs. 
Dictionaries are also known as associative arrays or hash maps in other programming languages.
"""

# Creating a dictionary:  enclose comma-separated key-value pairs within curly braces {} or by using the dict() constructor.
# Empty dictionary    # this is not an empty set as one may confuse it to be.
empty = {}
# an empty set is created using the set() constructor only.
print(type(empty))

dictio = {'key1': 'value1', 'key2': 'value2'}

# Using dict() constructor
dictio = dict()
dictio = dict(key1='value1', key2='value2')
"""
Accessing Elements
You can access the values in a dictionary by providing the corresponding key inside square brackets []. 
If the key is not found, it will raise a KeyError. 
Alternatively, you can use the get() method, which returns None (or a specified default value) if the key is not found.
"""
customer = {'fruit': 'Mango', 'price': 250}

print(customer['fruit'])
print(customer.get('price'))
print(customer.get('address'))
print(customer.get('address', 'Unknown'))  # Output: Unknown (default value)

# Getting a list of keys
customer.keys()

# Exercise One: using values()
customer.values()

# Exercise Two: check if a key exists in a dictionary
print('fruit' in customer)
print('age' in customer)

# Exercise Three: Give an example on how to change dictionary items, how to update
"""
Modifying values:
You can modify the value associated with a specific key by assigning a new value to it.
"""
customer['price'] = 300
print(customer)

# Exercise Four: Give an example on how to add dictionary items, how to remove them
"""
Adding and removing key-value pairs:
To add a new key-value pair, you can simply assign a value to a new key. 
To remove a key-value pair, you can use the del keyword or the pop() method.
"""
person = {"name": "Ellie", "age": 19, "city": "Albion",
          "country": "UK", "hobbies": ["reading", "traveling", "painting"]}

print(person)

person['address'] = 'Makerere'
print(person)

del person['age']
print(person)

person.pop('hobbies')
print(person)

# Exercise Five: Give an example on how to loop through a dictionary and how to nest dictionaries
# Iterating over a dictionary:
# You can iterate over the keys, values, or key-value pairs in a dictionary using the keys(), values(), or items() methods, respectively.
for key in person.keys():
    print(key)

for value in person.values():
    print(value)

for key, value in person.items():
    print(key, value)

# Nesting dictionaries in Python refers to the practice of storing dictionaries as values within another dictionary.
# Creating a nested dictionary
student = {
    "name": "Silver",
    "age": 20,
    "grades": {
        "math": 95,
        "english": 85,
        "science": 92
    }
}

# Accessing nested dictionary values
print(student["name"])
print(student["grades"]["math"])


#  NUMBERS.
# integers, floats, complex
a = 2  # int
b = 2.0  # float
c = 23 + 2j  # complex

print(type(a))
print(type(b))
print(type(c))

# Integers  .. all whole numbers including negatives
d = 20
e = -3
print(type(d))
print(type(e))

# Floats  ..  all numbers with a decimal point
f = 2.0
g = -3.7
print(type(f))
print(type(g))

# Complex numbers  ..  numbers with an imaginary part
h = -1j    # -j is not complex
i = -1 + 4j
print(type(h))
print(type(i))

# Convert from int to complex
z = complex(d)
print(z)
print(type(z))

# Convert from float to complex
y = complex(f)
print(y)
print(type(y))

"""
Exercise: Convert from complex to float
To convert a complex number to a float, you need to extract the real or imaginary part explicitly.
"""
m = float(i.real)
print(m)
print(type(m))

# Convert int to float
r = float(d)
print(r)
print(type(r))


#  CASTING.
# Casting refers to the process of converting one data type to another.

h = int(20)
a = int("234")

print(h)
print(a)
print(type(a))

"""
STRINGS.
Strings are immutable
"""
car = "Aston Martin"    # String creation

# Multi line strings
saf = """This 
is a multi line 
string"""
print(saf)

# Accessing characters in a string:
print(car[0])
print(car[6])
print(car[-1])

# String concatenation
string1 = "Good"
string2 = "morning"
concatenated_string = string1 + " " + string2
print(concatenated_string)

# Exercise one: Use the len() function
# String length
# returns the number of characters (including whitespace and special characters) in the string.
print(len(car))

# Exercise two: Use a for loop in a string
for char in car:
    print(char)

# Exercise three: Give an example of slicing in strings
# String slicing
print(car[6:10])
print(car[:5])
print(car[6:])

# String methods
print(car.upper())
print(car.lower())
print(car.startswith("A"))   # returns true or false
print(car.split(" "))

# String formatting
country = "Uganda"
year = 1962
formatted_string = "{} got its independence in {}.".format(country, year)
print(formatted_string)

# this example shows you that variables must first be defined
# print('{} is my favorite sport'.format(element))      # will return a NameError
element = 'Football'

# STRING MANIPULATION.
# .title() ..  title method capitalizes all first letters in each word of a string.
explorer = "john speke"
print(explorer.title())

# .replace()  .. takes in two values, one that it searches for and the other that it replaces the searched value with
# replacing an exclamation point with a period
words = "Hello there!"
print(words.replace("!", "."))

# .find()  ..  find method will search for any string we ask it to.
greet = "A good afternoon to you."

index = greet.find("o")
print(index)   # Output: 3

index = greet.find("you")
print(index)   # Output: 7

index = greet.find("Python")
print(index)   # Output: -1

# .strip()  ..  can be used to get rid of a certain character on the left and right side of a string. By default, it will remove spaces.
require = "   Try to miss that hurdle   "

stripped_string = require.strip()
print(stripped_string)

requi = "...Try to miss that hurdle..."
stripped_string = requi.strip(".")
print(stripped_string)

left_stripped_string = requi.lstrip(".")   # using lstrip()
print(left_stripped_string)

right_stripped_string = requi.rstrip(".")  # using rstrip()
print(right_stripped_string)

# Exercise four: How do you remove a space in a string
# Removing space between a single string
stri = "After noon"
print(stri.replace(" ", ""))


# BOOLEANS.
# The bool type is used to represent boolean values, which can be either True or False
print(20 > 32)
print(20 == 32)
print(20 < 45)

print(bool(34))

print(bool(0))  # returns false

print(bool({}))  # empty set returns false

# Exercise: Use a condition to show how to use booleans.
# Check if a number is positive, negative, or zero
number = -5

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
