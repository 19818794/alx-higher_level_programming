# Python - Inheritance

The aim is to learn about inheritance, what is a superclass, baseclass or parentclass, subclass, the default class every class inherits from, and the purpose of inheritance. Also, what are, when, and how to use isinstance, issubclass, type, and super built-in functions?

# Technologies

Tested on Ubuntu 20.04 LTS.

Python Scripts are written with python3 (version 3.8.5).

# Files

All of the following files are programs written in Python:

| Filename                    | Description
|:---------------------------:| ------------------------------------------------------------------------------------------------ 
| `0-lookup.py`               | creates a function that returns the list of available attributes and methods of an object.
| `1-my_list.py`              | creates a class MyList that inherits from the list.
| `tests/1-my_list.txt`       | interactive tests for the module `1-my_list.py`.
| `2-is_same_class.py`        | creates a function that checks if the object is exactly an instance of the specified class.
| `3-is_kind_of_class.py`     | creates a function that checks if the object is an instance of, or if the object is an instance of a class that is inherited from the specified class.
| `4-inherits_from.py`        | creates a function that checks if the object is an instance of a class that was inherited (directly or indirectly) from the specified class.
| `5-base_geometry.py`        | creates an empty class BaseGeometry.
| `6-base_geometry.py`        | creates a class BaseGeometry based on `5-base_geometry.py` with a public instance method.
| `7-base_geometry.py`        | creates a class BaseGeometry based on `6-base_geometry.py` with a second public instance method.
| `tests/7-base_geometry.txt` | interactive tests for the module `7-base_geometry.py`.
| `8-rectangle.py`            | creates a class Rectangle that inherits from BaseGeometry `7-base_geometry.py` to validate width and height inetegers.
| `9-rectangle.py`            | creates a class Rectangle based on `8-rectangle.py` to validate width and height integers, and get the area and string representation of a rectangle.
