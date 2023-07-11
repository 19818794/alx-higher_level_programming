#!/usr/bin/python3
"""
1-my_list module.
"""


class MyList(list):
    """
    a class MyList that inherits from list.
    """
    def __init__(self):
        """
        initialize an instance.
        """
        super().__init__()

    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort).
        """
        print(sorted(self))
