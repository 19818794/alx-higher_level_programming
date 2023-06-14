#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    It replaces all occurrences of an element by another in a new list.
    Arguments:
        my_list: is the initial list.
        search: is the element to replace in the list.
        replace: is the new element.
    Returns:
        A new list.
    """
    new_list = [elem if elem != search else replace for elem in my_list]
    return new_list
