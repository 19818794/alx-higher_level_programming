# Python - Almost a circle

The aim is to learn how to implement Unit testing in a large project, serialize and deserialize a Class, write and read a JSON file, and handle named arguments in a function. Also, learn what is *args and  **kwargs and how to use them.

# Background Context

This project is a review for everything about Python:

Import

Exceptions

Class

Private attribute

Getter/Setter

Class method

Static method

Inheritance

Unittest

Read/Write file

Also we will learn about:

args and kwargs

Serialization/Deserialization

JSON

# Technologies

Tested on Ubuntu 20.04 LTS.

Python Scripts are written with python3 (version 3.8.5).

# Files

All of the following files are programs written in Python:

| Filename                         | Description
|:--------------------------------:| -------------------------------------------------------------------------------------------- 
| `models/__init__.py`             | creates an empty file inside `models` folder, so this folder will become a Python package.
| `models/base.py`                 | creates a class  to manage id attribute in all your future classes and to avoid duplicating the same code.
| `models/rectangle.py`            | creates a class Rectangle that inherits a public instance attribute object identifier from Base `models/base.py` and creates its private attributes with getter/setter to protect the Rectangle class attributes. Also, it creates a validation function of all setter methods and instantiation. It creates a public method that returns the area value of the Rectangle instance.
| `tests/__init__.py`              | creates an empty file inside `tests` folder, so this folder will become a Python package.
| `tests/test_models/__init__.py`  | creates an empty file inside `tests/test_models` folder, so this folder will become a Python package.
| `tests/test_models/test_base.py` | unittests for the module `models/base.py`.
| `tests/test_models/test_rectangle.py` | unittests for the module `models/rectangle.py`.
| `0-main.py`                           | main program 0.
| `1-main.py`                           | main program 1.
| `2-main.py`                           | main program 2.
| `3-main.py`                           | main program 3.

# File structure

* models:
	* \_\_init\_\_.py
	* base.py
	* rectangle.py

* tests:
	* \_\_init\_\_.py
	* test_models:
		* \_\_init\_\_.py
		* test_base.py
		* test_rectangle.py

* 0-main.py
* 1-main.py
* 2-main.py
* 3-main.py
