# Python - More Classes and Objects

The aim is to learn about what is OOP, a class, an object, an instance, an attribute, a self, a method, a property, a class attribute, a class method, and a static method.

Also, what is the difference between a class and an object or instance, between an attribute and a property in Python, and between an object attribute and a class attribute?

What are the special __init__, __str__, and __repr__ methods, how to use them, and the difference between them?

What are and how to use public, protected, and private attributes? How to bind attributes to objects and classes and how does Python find the attributes of an object or class?

# Technologies

Tested on Ubuntu 20.04 LTS.

Python Scripts are written with python3 (version 3.8.5).

# Files

All of the following files are programs written in Python:

| Filename         | Description
|:----------------:| -------------------------------------------------------------------------------------------------------------- 
| `0-rectangle.py` | creates an empty class Rectangle that defines a rectangle.
| `1-rectangle.py` | creates a class Rectangle with two private instance attributes, their properties and setters, and instantiation based on `0-rectangle.py`.
| `2-rectangle.py` | creates two public instance methods based on `1-rectangle.py`.
| `3-rectangle.py` | creates a string representation based on `2-rectangle.py`.
| `4-rectangle.py` | creates `__repr__` function to be able to recreate a new instance by using eval() based on `3-rectangle.py`.
| `5-rectangle.py` | creates `__del__` function to print the message `Bye rectangle...` when an instance of Rectangle is deleted based on `4-rectangle.py`.
| `6-rectangle.py` | creates a public class attribute based on `5-rectangle.py`.
| `7-rectangle.py` | creates a second public class attribute based on `6-rectangle.py`.
| `8-rectangle.py` | creates a static method based on `7-rectangle.py`.
| `9-rectangle.py` | creates a class method based on `8-rectangle.py`.
