class LinkedListException(Exception):
    """
    This class is used for giving more informative Exceptions.
    """
    pass


class LinkedList:
    """
    A linked list is either empty or a list cell, which
    has a value and a link to another linked list, the 'tail' of the list.
    This is an abstract class; you cannot make any direct
    instances of it. Use Cell or Empty instead.
    Most of the methods are implemented in subclasses.
    """

    def is_empty(self):
        """Returns true, if the linked list has no elements, otherwise false"""
        pass

    def length(self):
        """Returns the length of the LinkedList."""
        pass

    def nth(self, n):
        """
        Returns the value of the nth cell in a LinkedList, counting from zero.
        Raises exception LinkedListException, if self is empty.
        """
        pass

    def index(self, x):
        """
        Returns the first index i in the linked list, where the value x is found. Returns None if none of the Cells
        has a value of x.

        Index 0 is the first element of the linked list.
        """
        pass


class Empty(LinkedList):
    """A singleton representing the empty list"""

    __instance = None

    def __new__(cls):
        """Creates a new singleton, if there is none. Returns the singleton."""
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            cls.__instance.name = "Empty"
        return cls.__instance

    def is_empty(self):
        return True

    def length(self):
        return 0

    def nth(self, n):
        """
        Returns the value of the nth cell in a LinkedList, counting from zero.
        Raises exception LinkedListException, if self is empty.
        """
        raise LinkedListException('The cell is empty')

    def index(self, x):
        """
        Returns the first index i in the linked list, where the value x is found. Returns None if none of the Cells
        has a value of x.

        The first element in the linked list has the index 0.
        """
        return None

    def __repr__(self):
        return 'Empty()'


class Cell(LinkedList):

    def __init__(self, value, tail):
        if not isinstance(tail, LinkedList):
            raise LinkedListException('Cannot construct a Cell using {} as the tail'.format(tail))
        self.value = value
        self.tail = tail

    def is_empty(self):
        return False

    def length(self):
        return 1 + self.tail.length()

    def nth(self, n):
        """
        Returns the value of the nth cell in a LinkedList, counting from zero.
        Raises exception LinkedListException, if self is empty.
        """

        if self.is_empty():
            raise LinkedListException('The cell is empty')
        else:
            if n == 0:
                return self.value
            else:
                return self.tail.nth(n - 1)

    def index(self, x):
        """
        Returns the first index i in the linked list, where the value x is found.
        Returns None if none of the Cells has a value of x.

        The first element in the linked list has the index 0.
        """
        try:
            if self.value == x:
                return 0
            else:
                if self.tail.is_empty():
                    return None
                else:
                    return 1 + self.tail.index(x)
        except TypeError:
            return None

    def __repr__(self):
        return 'Cell({}, {})'.format(self.value, self.tail)
