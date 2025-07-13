#!/usr/bin/python3
"""This module defines a Square class with size property and area calculation."""


class Square:
    """Square class with a private size attribute and property methods."""

    def __init__(self, size=0):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square (default 0).
        """
        self.size = size  # setter vasitəsilə təyin edilir

    @property
    def size(self):
        """Retrieve the size of the square (getter)."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square (setter) with validation.

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
