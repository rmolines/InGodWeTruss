# -*- coding: utf-8 -*-
__author__  = "Matheus Marotzke"
__copyright__ = "Copyright 2017, Matheus Marotzke"
__license__ = "GPLv3.0"


class Truss:
    """Class that represents the Truss and it's values"""

    def __init__(self, nodes, elements):
        self.nodes    = nodes    # List of nodes in the Truss
        self.elements = elements # List of elements in the Truss

    def __repr__(self):
        # Method to determine string representation of a Node
        string = "Truss: Elements:" + str(self.elements) + ' Nodes:' + str(self.nodes)
        return string

    def calc_global_stiffness_matrix(self): #TODO - Implement this
        # Method to generate the k_global matrix
        return
