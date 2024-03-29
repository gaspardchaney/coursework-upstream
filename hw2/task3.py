"""
CMSC 14200, Spring 2024
Homework #2

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""
from typing import Optional

class BSTEmptyOpt:
    """
    Empty optimized BST
    """
    @property
    def is_empty(self) -> bool:
        """
        True if the tree is empty, False otherwise
        """
        return True

    @property
    def is_leaf(self) -> bool:
        """
        True if the tree is a leaf, False otherwise
        """
        return False

    @property
    def num_nodes(self) -> int:
        """
        Number of nodes in the tree
        """
        return 0

    @property
    def height(self) -> int:
        """
        Height of the tree
        """
        return 0

    @property
    def span(self) -> Optional[tuple[int, int]]:
        """
        Span of the tree: A tuple with the minimum and maximum values in the
            tree, or None if the tree is empty
        """
        return None

    def contains(self, n: int) -> bool:
        """
        Determines whether a value is contained in the tree.

        Input:
            n (int): The value to check

        Returns: True if n is in the tree, False otherwise.
        """
        return False

    def insert(self, n: int) -> "BSTNodeOpt":
        """
        Insert a value into the tree.

        Input:
            n (int): The value to insert

        Returns: A new tree with n inserted.
        """
        return BSTNodeOpt(n, BSTEmptyOpt(), BSTEmptyOpt())

class BSTNodeOpt:
    """
    Optimized BST tree node
    """

    value: int
    left: "BSTEmptyOpt | BSTNodeOpt"
    right: "BSTEmptyOpt | BSTNodeOpt"

    def __init__(self, value: int,
                       left: "BSTEmptyOpt | BSTNodeOpt",
                       right: "BSTEmptyOpt | BSTNodeOpt"):
        """
        Constructor.

        Input:
            value: Value associated with the tree node
            left: Left child tree
            right: Right child tree
        """
        self.value = value
        self.left = left
        self.right = right

    @property
    def is_empty(self) -> bool:
        """
        True if the tree is empty, False otherwise
        """
        return False

    @property
    def is_leaf(self) -> bool:
        """
        True if the tree is a leaf, False otherwise
        """
        return self.left.is_empty and self.right.is_empty

    @property
    def num_nodes(self) -> int:
        """
        Number of nodes in the tree
        """
        return 1 + self.left.num_nodes + self.right.num_nodes

    @property
    def height(self) -> int:
        """
        Height of the tree
        """
        return 1 + max(self.left.height, self.right.height)

    @property
    def span(self) -> Optional[tuple[int, int]]:
        """
        Span of the tree: A tuple with the minimum and maximum values in the
            tree, or None if the tree is empty
        """
        left_span = self.left.span
        right_span = self.right.span
        min = self.value
        max = self.value
        if left_span is not None:
            min = left_span[0]
        if right_span is not None:
            max = right_span[1]
        return (min, max)

    @property
    def balance_factor(self) -> int:
        """
        Balance factor of the tree
        """
        return self.right.height - self.left.height

    def contains(self, n: int) -> bool:
        """
        Determines whether a value is contained in the tree.

        Input:
            n (int): The value to check

        Returns: True if n is in the tree, False otherwise.
        """
        if n < self.value:
            return self.left.contains(n)
        elif n > self.value:
            return self.right.contains(n)
        else:
            return True

    def insert(self, n: int) -> "BSTNodeOpt":
        """
        Insert a value into the tree.

        Input:
            n (int): The value to insert

        Returns: A new tree with n inserted.
        """
        if n < self.value:
            return BSTNodeOpt(self.value, self.left.insert(n), self.right)
        elif n > self.value:
            return BSTNodeOpt(self.value, self.left, self.right.insert(n))
        else:
            return self
