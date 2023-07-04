# Python - Everything is object

The aim of this project is to look a little bit closer at how Python works with different types of objects.

This project is a little bit different than the usual projects.

The first part is only questions about Python's specificity like "What would be the result of…".

It's important to truly understand the reasons behind the answers of all those tasks so that we can apply the same logic to other variables and other variable types.

Note that during interviews for Python positions, we will most likely have to answer to these type of questions.

# Technologies

Tested on Ubuntu 20.04 LTS.

Python Scripts are written with python3 (version 3.8.5).

# Files

All of the following files are programs written in Python and txt:

| Filename         | Description
|:----------------:| -------------------------------------------------------------------------------------------------------------- 
| `0-answer.txt`   | What function would you use to get the type of an object? Write the name of the function in the file, without ().
| `1-answer.txt`   | How do you get the variable identifier (which is the memory address in the CPython implementation)? Write the name of the function in the file, without ().
| `2-answer.txt`   | In the following code, do a and b point to the same object? Answer with Yes or No. `>>> a = 89` `>>> b = 100`.
| `3-answer.txt`   | In the following code, do a and b point to the same object? Answer with Yes or No. `>>> a = 89` `>>> b = 89`.
| `4-answer.txt`   | In the following code, do a and b point to the same object? Answer with Yes or No. `>>> a = 89` `>>> b = a`.
| `5-answer.txt`   | In the following code, do a and b point to the same object? Answer with Yes or No. `>>> a = 89` `>>> b = a + 1`.
| `6-answer.txt`   | What do these 3 lines print? `>>> s1 = "Best School"` `>>> s2 = s1` `>>> print(s1 == s2)`.
| `7-answer.txt`   | What do these 3 lines print? `>>> s1 = "Best"` `>>> s2 = s1` `>>> print(s1 is s2`.
| `8-answer.txt`   | What do these 3 lines print? `>>> s1 = "Best School"` `>>> s2 = "Best School"` `>>> print(s1 == s2)`.
| `9-answer.txt`   | What do these 3 lines print? `>>> s1 = "Best School"` `>>> s2 = "Best School"` `>>> print(s1 is s2)`.
| `10-answer.txt`  | What do these 3 lines print? `>>> l1 = [1, 2, 3]` `>>> l2 = [1, 2, 3] ` `>>> print(l1 == l2)`.
| `11-answer.txt`  | What do these 3 lines print? `>>> l1 = [1, 2, 3]` `>>> l2 = [1, 2, 3]` `>>> print(l1 is l2)`.
| `12-answer.txt`  | What do these 3 lines print? `>>> l1 = [1, 2, 3]` `>>> l2 = l1` `>>> print(l1 == l2)`.
| `13-answer.txt`  | What do these 3 lines print? `>>> l1 = [1, 2, 3]` `>>> l2 = l1` `>>> print(l1 is l2)`.
| `14-answer.txt`  | What does this script print? `l1 = [1, 2, 3]` `l2 = l1` `l1.append(4)` `print(l2)`.
| `15-answer.txt`  | What does this script print? `l1 = [1, 2, 3]` `l2 = l1` `l1 = l1 + [4]` `print(l2)`.
| `16-answer.txt`  | What does this script print? `def increment(n): n += 1` `a = 1` `increment(a)` `print(a)`.
| `17-answer.txt`  | What does this script print? `def increment(n): n.append(4)` `l = [1, 2, 3]` `increment(l)` `print(l)`.
| `18-answer.txt`  | What does this script print? `def assign_value(n, v): n = v` `l1 = [1, 2, 3]` `l2 = [4, 5, 6]` `assign_value(l1, l2)` `print(l1)`.
| `19-copy_list.py` | returns a copy of a list that can contain any type of objects.
| `20-answer.txt`   | `a = ()` Is a tuple? Answer with Yes or No.
