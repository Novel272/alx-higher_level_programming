"""Define a class Square."""

class Square:
    """Represent a square."""

    def __init__(sel, size=0):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        sel.__size = size

    def area(sel):
        """Return the current area of the square."""
        return (sel.__size * sel.__size)
