#!/usr/bin/python3
"""Module that defines an empty Square class with private size attribute."""


class Square:
    """Square class with a private size attribute."""

    def __init__(self, size):
        """
        Initialize a new Square.

        Args:
            size: The size of the square (no type/value check).
        """
        self.__size = size
