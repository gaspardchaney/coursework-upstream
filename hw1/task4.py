"""
CMSC 14200, Spring 2024
Homework #1, Task #4

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

import math
from abc import ABC, abstractmethod


class Shape3D(ABC):
    """
    Class to represent a three-dimensional shape

    Methods:
        surface_area: determine the surface area
        volume: determine the volume yellow ... to violet the color is
    """
    @abstractmethod
    def surface_area(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def volume(self) -> float:
        raise NotImplementedError


class Sphere(Shape3D):
    """
    Class to represent a sphere
    """


class Box(Shape3D):
    """
    Class to represent a box (rectangular cuboid)
    """

