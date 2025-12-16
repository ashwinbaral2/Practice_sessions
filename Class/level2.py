# ===============================
# Python Classes & Objects
# Level 2 Practice Questions
# ===============================

# Q1.
# Create a class named Student.
# The class should be empty.
# ----------------------------------------------

class Student:
    {}


print(Student)
# ----------------------------------------------
# Q2.
# Create a class Car.
# Create an object called my_car.
# ----------------------------------------------


class Car:
    my_car = {
        "Name": "Toyota",
        "Model": "Corolla",
        "Price": "20 Lakhs"
    }


# ----------------------------------------------

# Q3.
# Create a class Dog.
# Add an attribute name = "Tommy".
# Create an object and print the name.
# ----------------------------------------------

class Dog:
    name = "Tommy"


print(Dog.name)

# ----------------------------------------------

# Q4.
# Create a class Person.
# Use __init__ to take name as input.
# Create an object and print the name.
# hint: class MyClass:
# def __init__(self, argument1, argument2):
#     self.argument1 = argument1
#     self.argument2 = argument2

# ----------------------------------------------


class person:
    def __init__(self, name):
        self.name = name
        print(f"The name is {name}")


person("Ashwin")
person("Barsha")
# ----------------------------------------------

# Q5.
# Create a class Book.
# Attributes: title, auhtor, price.
# Create object and print all values.
# ----------------------------------------------


class book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        print(f"{title} book by {author} will cost you {price}.")


book("Saya", "Subin Bhattrai", 380)
book("Bhagavad Gita", "Veda Vyasa", 600)

#Output:   Saya book by Subin Bhattrai will cost you 380.
#          Bhagavad Gita book by Veda Vyasa will cost you 600.

# ----------------------------------------------

# Q6.
# Create a class Calculator.
# Add a method add() that prints the sum of 2 and 3.
# Call the method using an object.
# ----------------------------------------------
class calc() :
    def add(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
        sum = num1 + num2
        print(f" The sum of two numbers will be {sum}")

c = calc()
c.add(2, 3)
c.add('chiku', 'taru')
# ----------------------------------------------

# Q7.
# Create a class Student.
# Attributes: name, marks.
# Create a method display() that prints name and marks.
# ----------------------------------------------
class Student() :
    def display(self, name, marks):
        self.name = name
        self.marks = marks
        print(f"Mr/Mrs {name}, You have scored {marks} out of 100 in the test.")

s = Student()
s.display("Ashwin", 40)#Mr/Mrs Ashwin, You have scored 40 out of 100 in the test.
s.display("Barsha", 80)#Mr/Mrs Barsha, You have scored 80 out of 100 in the test.

# ----------------------------------------------

# Q8.
# Create a class Laptop.
# Attribute: brand.
# Create an object.
# Change the brand using the object and print it.
# ----------------------------------------------
class Laptop():
    def buy(self, brand):
        self.brand = brand
        print(f" Laptop Brand : {brand} ")

b = Laptop()


# ----------------------------------------------

# Q9.
# Create a class Phone.
# Attribute: model.
# Create two different objects with different models.
# Print both models.
# ----------------------------------------------


# ----------------------------------------------

# Q10.
# Create a class Animal.
# Add a method speak() that prints "Animal makes a sound".
# Create an object and call the method.
# ----------------------------------------------


# ----------------------------------------------
