#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(sel, size):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        sel.size = size

    @property
    def size(sel):
        """Get/set the current size of the square."""
        return (sel.__size)

    @size.setter
    def size(sel, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        sel.__size = value

    def area(sel):
        """Return the current area of the square."""
        return (sel.__size * sel.__size)

    def my_print(sel):
        """Print the square with the # character."""
        for i in range(0, sel.__size):
            [print("#", end="") for j in range(sel.__size)]
            print("")
        if sel.__size == 0:
            print("")
