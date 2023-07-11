#!/usr/bin/python3
"""
7-add_item module contains a script that adds all arguments
to a Python list, and then save them to a file.
"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
python_list = []
try:
    python_list = load_from_json_file(filename)
except Exception:
    save_to_json_file(python_list, filename)
len_argv = len(argv)
if len_argv > 1:
    for i in range(1, len_argv):
        python_list.append(argv[i])
    save_to_json_file(python_list, filename)
