# -*- coding: utf-8 -*-
__author__  = "Matheus Marotzke"
__copyright__ = "Copyright 2017, Matheus Marotzke"
__license__ = "GPLv3.0"

from itertools import count

class Node:
    """Class that represents a Node from a Truss"""
    _ids = count(0) # Counts every new object instance

    def __init__(self, x, y, fd_x = None, fd_y = None):
        self.id   = self._ids.next() # Element's ID
        self.fd_x = fd_x             # FreedomDegree object / (fd_x.direction == 0)
        self.fd_y = fd_y             # FreedomDegree object / (fd_y.direction == 1)
        self.x    = x                # Coordinate X of the Node
        self.y    = y                # Coordinate Y of the Node

    def __repr__(self):
        # Method to determine string representation of a Node
        string = str(self.id) + ': x=' + str(self.x) + " y=" + str(self.y)
        return string
