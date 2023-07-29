# DAY3 EVENING
print("\n")
print('*' * 25 + 'Exercise.1' + '*' * 25)
# Exercise.1
# QN.1 Create list of 5 names and output 2nd item
names = ["Emily", "Jacob", "Sophia", "Liam", "Olivia"]
second_name = names[1]
print(second_name)

# QN.2  Write a python program to change the value of the first item to a new value
new_value = "Ethan"

names[0] = new_value

print(names)

# QN.3  Write a python program to add a sixth item to the list
new_name = "Benjamin"

names.append(new_name)

print(names)

# QN.4  Write a python program to add “Bathel” as the 3rd item in your list
new_name = "Bathel"

names.insert(2, new_name)

print(names)

# QN.5  Write a python program to remove the 4th item from the list
removed_name = names.pop(3)

print("Removed item:", removed_name)
print("Updated list:", names)

# QN.6  Use negative indexing to print the last item in your list
last_name = names[-1]

print("Last name:", last_name)

# QN.7  Create a new list with 7 items and use a range of indexes to print the 3rd, 4th and 5th items.
items = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape"]

# Using range of indexes 2, 3, 4
selected_items = items[2:5]

print(selected_items)

# QN.8  Write a list of countries and make a copy of it.
countries = ["United States", "Canada", "United Kingdom", "Germany", "France"]
countries_copy = countries.copy()

print("Original list:", countries)
print("Copied list:", countries_copy)

# QN.9  Write a python program to loop through the list of countries
for country in countries:
    print(country)

# QN.10  Write a list of animal names and sort them in both descending and ascending order
animals = ["Lion", "Elephant", "Tiger", "Giraffe", "Monkey"]

# Sort in ascending order
animals_asc = sorted(animals)

# Sort in descending order
animals_desc = sorted(animals, reverse=True)

print("Ascending order:", animals_asc)
print("Descending order:", animals_desc)

# QN.11  Output only animal names with the letter ‘a’ in them
# Filter animal names with letter 'a'
animals_with_a = [animal for animal in animals if 'a' in animal.lower()]

print("Animal names with 'a':", animals_with_a)

# QN.12  Write two lists, one containing your first names and the other your second names. Join the two lists
first_names = ["John", "Emma", "Michael", "Sophia"]
last_names = ["Smith", "Johnson", "Williams", "Brown"]

full_names = []
for first, last in zip(first_names, last_names):
    full_names.append(first + " " + last)

print("Full Names:", full_names)

print("\n")
print('*' * 25 + 'Exercise.2' + '*' * 25)

# Exercise.2
# QN.1  Given the tuple below print your favorite phone brand.
x = ("Samsung", "iPhone", "Tecno", "Redmi")
print(x[2])

# QN.2 Use negative indexing to print 2nd last item
second_last_item = x[-2]

print("Second last item:", second_last_item)

# QN.3  Update iphone to itel
x_list = list(x)

x_list[1] = "itel"
x = tuple(x_list)

print(x)

# QN.4  Add huawei to the tuple
z = list(x)
z.append("Huawei")
x = tuple(z)
print(x)

# QN.5  Loop through the tuple
for item in x:
    print(item)

# QN.6  Remove first element in the tuple
my_list = list(x)
del my_list[0]

x = tuple(my_list)
print(x)

# QN.7  Create tuple of cities
cities = tuple(["New York", "Paris", "Tokyo", "London"])

print(cities)

# QN.8  Unpack the tuple
# Unpacking a tuple means assigning its individual elements to separate variables.
city1, city2, city3, city4 = cities

print("City 1:", city1)
print("City 2:", city2)
print("City 3:", city3)
print("City 4:", city4)

# QN.9  Use range of indexes to print 2nd , 3rd and 4th cities
selected_cities = cities[1:4]

print("Selected cities:", selected_cities)

# QN.10  Join two tuples of names
names1 = ("John", "Emma", "Michael")
names2 = ("Sophia", "William", "Olivia")

joined_names = names1 + names2

print(joined_names)

# QN.11  Create tuple of colors and multiply it by 3
colors = ("Red", "Blue", "Green")
multiplied_colors = colors * 3

print(multiplied_colors)

# QN.12 Return number of times 8 appears in the tuple
my_tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count = my_tuple.count(8)

print("Number of times 8 appears:", count)

print("\n")
print('*' * 25 + 'Exercise.3' + '*' * 25)

# EXERCISE 3
# QN.1 Use the set() constructor to create a set of 3 of your favorite beverages.
beverages = set(["Coffee", "Tea", "Juice"])

print(beverages)

# QN.2  Use the correct method to add 2 more items to the beverages set.
beverages.add("Water")
beverages.add("Soda")

print(beverages)

# QN.3  Check if microwave is present in the set.
mySet = {"oven", "kettle", "microwave", "refrigerator"}

if "microwave" in mySet:
    print("Microwave is present in the set.")
else:
    print("Microwave is not present in the set.")

# QN.4  Write a python program to remove “kettle” from the set
mySet.remove("kettle")

print(mySet)

# QN.5  Write a python program to loop through the set above
for item in mySet:
    print(item)

# QN.6 Write a set of 4 items and a list of two items. Write a python program to add elements in the list to elements in the set.
mySet = {"apple", "banana", "orange", "grape"}
myList = ["kiwi", "mango"]

mySet.update(myList)

print(mySet)

# QN.7  Write two sets, one containing your ages and the other your first names. Join the two sets.
ages = {25, 30, 35, 40}
names = {"John", "Emma", "Michael", "Sophia"}

joined_set = ages.union(names)

print(joined_set)

print("\n")
print('*' * 25 + 'Exercise.4' + '*' * 25)

# EXERCISE 4
# QN.1 Declare two variables, an integer and a string and use the correct method to concatenate the two variables.
integer_var = 10
string_var = "Hello"

concatenated_var = str(integer_var) + " " + string_var

print(concatenated_var)

# QN.2 Output the string without spaces at the beginning, in the middle and at the end.
txt = "   Hello,    Uganda!   "
trimmed_string = txt.strip().replace(" ", "")
print(trimmed_string)

# QN.3 Write a python program to convert the value of ‘txt’ to uppercase
print(trimmed_string.upper())

#  QN.4 Write a python program to replace character ‘U’ with ‘V’ in the string above.
print(trimmed_string.replace("U", "V"))

# QN.5  o return a range of characters in the 2nd, 3rd and 4th position
y = "I am proudly Ugandan"
characters_range = y[1:4]

print(characters_range)

# QN.6 Write a python program to correct error in x = “All “Data Scientists” are cool!”
x = 'All "Data Scientists" are cool!'
print(x)

print("\n")
print('*' * 25 + 'Exercise.5' + '*' * 25)

# EXERCISE 5
# QN.1 print the value of the shoe size
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

shoe_size = Shoes["size"]
print("Shoe size:", shoe_size)

# QN.2  change the value “Nick” to “Adidas”
Shoes["brand"] = "Adidas"

print(Shoes)

# QN.3  add a key/value pair "type”: "sneakers"
Shoes["type"] = "sneakers"
print(Shoes)

# QN.4 return a list of all the keys
print(Shoes.keys())

# QN.5  return a list of all the values
print(Shoes.values())

# QN.6  Check if the key “size” exists in the dictionary
if "size" in Shoes:
    print("The key 'size' exists in the dictionary.")
else:
    print("The key 'size' does not exist in the dictionary.")

# QN.7 loop through the dictionary
for key, value in Shoes.items():
    print(key, ":", value)

# QN.8  remove “color” from the dictionary.
Shoes.pop("color")
print(Shoes)

# QN.9  empty the dictionary
Shoes.clear()
print(Shoes)

# QN.10  Write a dictionary of your choice and make a copy of it.
original_dict = {"name": "John", "age": 30, "city": "New York"}

copied_dict = original_dict.copy()

# Print both dictionaries
print("Original Dictionary:", original_dict)
print("Copied Dictionary:", copied_dict)

# QN.11   Write a python program to show nested dictionaries
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
