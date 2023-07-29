# OBJECT ORIENTED PROGRAMMING IN PYTHON.
"""
Classes
Objects 
Inheritance
Polymorphism
Encapsulation
Abstraction

CLASSES
Classes are used to create objects that encapsulate data and the operations that can be performed on that data.
Classes are defined using the class keyword, and they serve as blueprints for creating instances or objects.
"""
# Example.1
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print("Engine started")

    def stop_engine(self):
        print("Engine stopped")

my_car = Car("Ferrari", "Ferr", "2023")
print(my_car.make)
print(my_car.model)
print(my_car.year)
my_car.start_engine()
my_car.stop_engine()

# Example.2 Bank Account
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful. New balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful. New balance:", self.balance)
        else:
            print("Insufficient funds.")

    def display_acc_No(self):
        print("Acccount Number: ", self.account_number)

# Creating an instance of the BankAccount class
account = BankAccount("12345", 2000)
account.deposit(1000)  
account.withdraw(500)  
account.withdraw(1000)  
account.display_acc_No()

# Example.3
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

# Creating an instance of the Rectangle class
rect = Rectangle(5, 3)
print(rect.length)
print(rect.width)
print(rect.calculate_area())  
print(rect.calculate_perimeter())  

# Example.4
class Student:
    def __init__(self, name, year, course):
        self.name = name
        self.year = year
        self.course = course

    def display_details(self):
        print("Name: ", self.name)
        print("Year: ", self.year)
        print("Course: ", self.course)

student1 = Student("Alice", 3, "Software")
student1.display_details()


# OBJECTS
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is", self.name,
              "and I am", self.age, "years old.")

person1 = Person("Julian", 85)

print(person1.name)  
print(person1.age)  
person1.greet()  

# EXERCISE.1
# Calculate area and circumference of a circle
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = math.pi * self.radius**2
        return area

    def calculate_circumference(self):
        circumference = 2 * math.pi * self.radius
        return circumference

# Create a circle instance
circle = Circle(5)  

# Calculate area and circumference
area = circle.calculate_area()
circumference = circle.calculate_circumference()

# Display the results
print("Area of the circle:", area)
print("Circumference of the circle:", circumference)


# EXERCISE.2
# Calculate and display employee bonuses(15%) of salary .. employee1: 150000, employee2: 230000
class Employee:
    def __init__(self, salary):
        self.salary = salary

    def calculate_bonus(self):
        bonus = self.salary * 0.15
        return int(bonus)


# Create employee instances
silver = Employee(150000)
john = Employee(230000)

# Calculate bonuses
Sbonus = silver.calculate_bonus()
Jbonus = john.calculate_bonus()

# Display bonuses
print("Silver's bonus is:", Sbonus)
print("John's bonus is:", Jbonus)


# ENCAPSULATION
"""
Goals of encapsulation are
1. Hide the internal implementation details of a class and provide a simple and consistent interface to interact with the object.
2.Control access to that data. 
You can define certain data members as private, which means they can only be accessed and modified within the class. 
3. Code organization and modularity
"""
# Example
class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        self.__account_number = account_number  # Private member
        self.__holder_name = holder_name  # Private member
        self.__balance = balance  # Private member

    def get_account_number(self):
        return self.__account_number

    def get_holder_name(self):
        return self.__holder_name

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        print("Deposit of", amount, "successful. New balance:", self.__balance)

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print("Withdrawal of", amount,
                  "successful. New balance:", self.__balance)
        else:
            print("Insufficient funds. Withdrawal failed.")

# Create a bank account instance
my_account = BankAccount("2A56", "Silver", 2000)

# Accessing account details through public methods
print("Account Number:", my_account.get_account_number())
print("Account Holder:", my_account.get_holder_name())
print("Account Balance:", my_account.get_balance())

# Making a deposit
my_account.deposit(2000)

# Making a withdrawal
my_account.withdraw(3000)
my_account.withdraw(5000)


# EXERCISE.3
# Convert temperature (37) from celcius to farenheit
class ConvertTemp:
    def __init__(self):
        self.__celsius = None
        self.__fahrenheit = None

    def set_celsius(self, celsius):
        self.__celsius = celsius

    def set_fahrenheit(self, fahrenheit):
        self.__fahrenheit = fahrenheit

    def get_celsius(self):
        return self.__celsius

    def get_fahrenheit(self):
        return self.__fahrenheit

    def convert_to_fahrenheit(self):
        self.__fahrenheit = (self.__celsius * 9/5) + 32

    def convert_to_celsius(self):
        self.__celsius = (self.__fahrenheit - 32) * 5/9

converter = ConvertTemp()

# Set the temperature in Celsius
converter.set_celsius(37)

# Convert Celsius to Fahrenheit
converter.convert_to_fahrenheit()

# Get the converted temperature in Fahrenheit
fahrenheit = converter.get_fahrenheit()
print("Temperature in Fahrenheit:", fahrenheit)

print("*" * 25)

# ASSIGNMENT.
# Show encapsulation with employee information to give a pay rise. (e.g salary from 850000 to 1000000)
class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def get_name(self):
        return self._name

    def get_salary(self):
        return self._salary

    def give_pay_rise(self, new_salary):
        self._salary = new_salary

employee = Employee("Walusimbi", 850000)

# Print the current employee information
print("Current Employee Information:")
print("Name:", employee.get_name())
print("Salary:", employee.get_salary())

# Give a pay rise to the employee
new_salary = 1000000
employee.give_pay_rise(new_salary)

# Print the updated employee information
print("\nUpdated Employee Information:")
print("Name:", employee.get_name())
print("New salary:", employee.get_salary())


# INHERITANCE
""" 
Inheritance is a feature that allows you to create a new class (called a derived class or subclass) 
that inherits attributes and methods from an existing class (called a base class or superclass).
The derived class can add or modify functionality, extending or specializing the behavior inherited from the base class.

To define a derived class that inherits from a base class, 
you specify the base class name in parentheses after the derived class name in the class definition.

class BaseClass:
    # Base class attributes and methods

class DerivedClass(BaseClass):
    # Derived class attributes and methods
"""
# Example.1   
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        super().speak()  # Accessing the base class definition
        print("Meow!")

# Creating objects of derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Calling the speak() method of derived classes
dog.speak()  # Output: Woof!
cat.speak()  # Output: Meow!

# Example.2
class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start_engine(self):
        print("Engine started.")

    def stop_engine(self):
        print("Engine stopped.")

class Car(Vehicle):
    def __init__(self, brand, color, num_wheels):
        super().__init__(brand, color)
        self.num_wheels = num_wheels

    def drive(self):
        print("Car is being driven.")

class Motorcycle(Vehicle):
    def __init__(self, brand, color):
        super().__init__(brand, color)

    def ride(self):
        print("Motorcycle is being ridden.")

# Creating objects of derived classes
car = Car("Toyota", "Red", 4)
motorcycle = Motorcycle("Honda", "Blue")

# Accessing attributes and calling methods
print(car.brand)  
print(motorcycle.color)  

car.start_engine()  
motorcycle.stop_engine()  

car.drive() 
motorcycle.ride()  

# Exercise.1  Calculate area of circle and perimeter of a rectangle.
class Shape:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, color, width, length):
        super().__init__(color)
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width + self.length)

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

rectangle = Rectangle("Blue", 4, 6)
circle = Circle("Red", 3)

print(rectangle.get_color())  
print(circle.get_color())  

print(rectangle.area()) 
print(rectangle.perimeter())
print(circle.area())  

# Example.3  Multiple Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

class Flyable:
    def fly(self):
        print(f"{self.name} is flying.")

class Bird(Animal, Flyable):
    def __init__(self, name):
        super().__init__(name)

bird = Bird("Sparrow")
bird.eat() 
bird.fly()  

# Method Overriding .. derived class provides its own implementation of a method already defined in the base class.
class Shape:
    def area(self):
        print("Calculating area in the base class.")

class Rectangle(Shape):
    def area(self):
        print("Calculating area of a rectangle.")

class Circle(Shape):
    def area(self):
        print("Calculating area of a circle.")

def dm(shape):
    shape.area()

shape = Shape()
rectangle = Rectangle()
circle = Circle()

dm(shape)
dm(rectangle)
dm(circle)


# POLYMORPHISM
"""
Refers to the ability of objects of different classes to respond to the same method calls, 
resulting in different behaviors based on their specific implementations. 
Polymorphism in Python is often achieved through method overriding and inheritance. 
""" 
# Method Overloading allows a class to have multiple methods with the same name but different (parameters) signatures.

class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        return "Roar!"
    
class Chettah(Animal):
    def make_sound(self):
        return "Chirrup!"
    
class Cow(Animal):
    def make_sound(self):
        return "Moo!"

# Create instances of different animals
lion = Lion("Buddy")
chettah = Chettah("Whiskers")
cow = Cow("Daisy")

# Call the make_sound() method on different animal instances
animals = [lion, chettah, cow]

for animal in animals:
    print(animal.name + ": " + animal.make_sound())

""" 
In this example, we define an abstract base class Animal, which has a common method make_sound(). 
The Lion, Chettah, and Cow classes inherit from Animal and override the make_sound() method with their specific implementations.
We then create instances of different animal classes and store them in a list. 
By iterating over the list and calling the make_sound() method on each animal, we achieve polymorphic behavior. 
Each animal instance responds to the method call with its own unique sound, even though the method call is the same for all animals.
"""

# ABSTRACTION
""" 
Allows you focus on essential features and hide them from unnecessary details.
Abstract Base Classes (ABC): Are a way to define abstract classes in Python. 
An abstract class cannot be instantiated directly but serves as a blueprint for derived classes. 
It defines a common interface that derived classes must implement. 
The abc module in Python provides the ABC metaclass 
and decorators like @abstractmethod to define abstract methods and enforce their implementation in subclasses.
"""
from abc import ABC, abstractmethod

# Abstract base class representing a Vehicle
class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand
    
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

# Concrete class representing a Car
class Car(Vehicle):
    def start(self):
        return f"{self.brand} car has started."
    
    def stop(self):
        return f"{self.brand} car has stopped."

# Concrete class representing a Bike
class Bike(Vehicle):
    def start(self):
        return f"{self.brand} bike has started."
    
    def stop(self):
        return f"{self.brand} bike has stopped."

# Create instances of Car and Bike
my_car = Car("Toyota")
my_bike = Bike("Honda")

# Accessing the start and stop methods without knowing the underlying implementation
print(my_car.start())  
print(my_bike.stop())  

# Exercise.2  Demonstrate abstraction by calculating area of a circle and rectangle
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width

my_circle = Circle(5)
my_rectangle = Rectangle(4, 6)

# Calculate and print the areas without knowing the underlying implementation
print("Area of the Circle:", my_circle.calculate_area())
print("Area of the Rectangle:", my_rectangle.calculate_area())


# Assignment.  Create a receipt printing program with GUI interface.
""" 
The receipt below requires input of an item, price and quantity. 
After adding all details for a particular item, you click on the add item button.
If you wish to add another item, you still enter the name,price and quantity. Click add button again.
Once you are done, click on the print receipt button to print the receipt. 
"""
import tkinter as tk

class ReceiptPrinterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Silver's Receipt Printer")

        # Create GUI elements
        self.label_item = tk.Label(root, text="Item:")
        self.label_item.grid(row=0, column=0, sticky="e")
        self.entry_item = tk.Entry(root)
        self.entry_item.grid(row=0, column=1)
        self.label_price = tk.Label(root, text="Price:")
        self.label_price.grid(row=1, column=0, sticky="e")
        self.entry_price = tk.Entry(root)
        self.entry_price.grid(row=1, column=1)

        self.label_quantity = tk.Label(root, text="Quantity:")
        self.label_quantity.grid(row=2, column=0, sticky="e")
        self.entry_quantity = tk.Entry(root)
        self.entry_quantity.grid(row=2, column=1)

        self.button_add = tk.Button(root, text="Add Item", command=self.add_item)
        self.button_add.grid(row=3, columnspan=2)

        self.button_print = tk.Button(root, text="Print Receipt", command=self.print_receipt)
        self.button_print.grid(row=4, columnspan=2)

        self.text_receipt = tk.Text(root, height=15, width=40)
        self.text_receipt.grid(row=5, columnspan=2)

        # Initialize receipt data
        self.receipt_items = []

    def add_item(self):
        item = self.entry_item.get()
        price = float(self.entry_price.get())
        quantity = int(self.entry_quantity.get())
        self.receipt_items.append((item, price, quantity))

        # Clear input fields
        self.entry_item.delete(0, tk.END)
        self.entry_price.delete(0, tk.END)
        self.entry_quantity.delete(0, tk.END)

    def print_receipt(self):
        self.text_receipt.delete(1.0, tk.END)

        # Display company information
        self.text_receipt.insert(tk.END, "\t{}\n".format("Silver Walusimbi, Inc."))
        self.text_receipt.insert(tk.END, "\t{}\n".format("356 Hamburg Jt."))
        self.text_receipt.insert(tk.END, "\t{}\n".format("Berlin, Germany"))
        self.text_receipt.insert(tk.END, "*" * 40 + "\n")

         # Add CASH RECEIPT row
        self.text_receipt.insert(tk.END, "\t{}\n".format("CASH RECEIPT"))
        self.text_receipt.insert(tk.END, "*" * 40 + "\n")

        # Display product information
        self.text_receipt.insert(tk.END, "\tItemName\tItemPrice\tQuantity\n")
        for item, price, quantity in self.receipt_items:
            self.text_receipt.insert(tk.END, "\t{}\t${}\t\t{}\n".format(item.title(), int(price) if price.is_integer() else price, quantity))
        self.text_receipt.insert(tk.END, "*" * 40 + "\n")

        # Calculate total
        total = sum(price * quantity for _, price, quantity in self.receipt_items)

        # Display total
        self.text_receipt.insert(tk.END, "\t\t\tTotal: ${}\n".format(int(total) if total.is_integer() else total))
        self.text_receipt.insert(tk.END, "*" * 40 + "\n")

        # Display message
        self.text_receipt.insert(tk.END, "\n{}\n".format("Thanks for shopping with us today!"))

# Create the main window
root = tk.Tk()

# Create the application
app = ReceiptPrinterApp(root)

# Start the main event loop
root.mainloop()
