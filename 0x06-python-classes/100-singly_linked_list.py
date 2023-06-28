#!/usr/bin/python3
"""
we are not allowed to import any module.
"""


class Node:
    """
    defines a node of a singly linked list.
    """
    def __init__(self, data, next_node=None) -> None:
        """
        initializes class attributes.
        args:
            data (int): integer indicateing the value of the linked list node.
            next_node (Node): pointing on the address of the  next node.
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """
        retrieves the size.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        sets a value to the data.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        retrieves the next_node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        sets an address to the next_node.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    defines a singly linked list.
    """
    def __init__(self) -> None:
        """
        initializes class attributes.
        args:
            head (Node): a private instance attribute.
        """
        self.__head = None

    def __str__(self) -> str:
        """
        print the entire list in stdout, one node number by line.
        """
        ptr = self.__head
        all_data_list = list()
        while ptr is not None:
            all_data_list.append(str(ptr.data))
            ptr = ptr.next_node
        return "\n".join(all_data_list)

    def sorted_insert(self, value):
        """
        inserts a new Node into the correct sorted position in the list
        in increasing order.
        args:
            value: value of the node.
        """
        if self.__head is None:
            self.__head = Node(value)
            return
        if value < self.__head.data:
            self.__head = Node(value, self.__head)
            return
        ptr_next, ptr_last = self.__head.next_node, self.__head
        while ptr_next is not None:
            if ptr_next.data > value:
                ptr_last.next_node = Node(value, ptr_next)
                return
            ptr_last = ptr_next
            ptr_next = ptr_next.next_node
        ptr_last.next_node = Node(value)
