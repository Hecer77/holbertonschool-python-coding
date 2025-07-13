#!/usr/bin/python3
"""Module that defines a Square class with size and print methods."""


class Square:
    """Square class with size validation and visual print."""

    def __init__(self, size=0):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square (default 0).
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using '#' character to stdout."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
