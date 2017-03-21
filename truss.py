# -*- coding: utf-8 -*-
__author__  = "Matheus Marotzke"
__copyright__ = "Copyright 2017, Matheus Marotzke"
__license__ = "GPLv3.0"

import numpy as np

class Truss:
    """Class that represents the Truss and it's values"""

    def __init__(self, nodes, elements):
        self.nodes    = nodes    # List of nodes in the Truss
        self.elements = elements # List of elements in the Truss

    def __repr__(self):
        # Method to determine string representation of a Node
        string = "Truss: Elements:" + str(self.elements) + ' Nodes:' + str(self.nodes)
        return string

    def calc_global_stiffness_matrix(self):
        # Method to generate the k_global matrix
        n_fd                    = self.elements[-1].node_1.fd_x._ids
        n_fd                    = n_fd.next()
        global_stiffness_matrix = np.zeros((n_fd, n_fd),dtype=float)
        for element in self.elements:                                   # Iterate along the elements from the Truss
            fd_ids = [element.node_1.fd_x.id,                           # Matrix with the ids from Element's FreedomDegrees
                      element.node_1.fd_y.id,
                      element.node_2.fd_x.id,
                      element.node_2.fd_y.id]
            for i in range(3):
                for j in range(3):
                    k = element.calc_element_stiffness_item(i,j)        # Calculate the individual item
                    global_stiffness_matrix[fd_ids[i]][fd_ids[j]] += k  # Assign it to the matrix super-position
        return global_stiffness_matrix
