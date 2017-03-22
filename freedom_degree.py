# -*- coding: utf-8 -*-
__author__  = "Matheus Marotzke"
__copyright__ = "Copyright 2017, Matheus Marotzke"
__license__ = "GPLv3.0"

from itertools import count

class FreedomDegree:
    """Class that indicates the Freedom Degrees of Nodes"""
    _ids = count(0) # Counts every new object instance

    def __init__(self, direction, blocked = False, load = 0, reaction = 0):
        self.id        = self._ids.next() # Element's ID
        self.blocked   = blocked          # Indicates whether or not the Degree is blocked
        self.load      = load             # Amount of load over that specific fd (x or y)
        self.direction = direction        # Indicates the direction (0 = 'x'; 1 = 'y')
        self.reaction  = reaction         # Reaction from that specific fd (x or y)

    def __repr__(self):
        # Method to determine string representation of a FreedomDegree
        if self.direction   == 0:
            direc = 'x'
        elif self.direction == 1:
            direc = 'y'
        string  = str(self.id) + ': blocked=' + str(self.blocked)
        string += " direction=" + direc
        string += " load=" + str(self.load)
        return string
