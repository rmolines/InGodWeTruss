# -*- coding: utf-8 -*-
__author__  = "Matheus Marotzke"
__copyright__ = "Copyright 2017, Matheus Marotzke"
__license__ = "GPLv3.0"

import numpy as np

class Truss:
    """Class that represents the Truss and it's values"""

    def __init__(self, nodes, elements):
        self.nodes                   = nodes    # List of nodes in the Truss
        self.elements                = elements # List of elements in the Truss
        self.n_fd                    = 0        # Number of freedom_degrees in the Truss
        self.global_stiffness_matrix = self.calc_global_stiffness_matrix()

    def __repr__(self):
        # Method to determine string representation of a Node
        string = "Truss: Elements:" + str(self.elements) + ' Nodes:' + str(self.nodes)
        return string

    def solve(self): #TODO - implement Reactions
        # Method to Solve Truss by calculating: Displacement, Element's Stress and Strain, Reaction
        self.calc_nodes_displacement()
        self.calc_nodes_reaction()
        self.calc_elements_stress()
        self.calc_elements_strain()

    def calc_global_stiffness_matrix(self):
        # Method to generate the stiffness global matrix
        element_fd = self.elements[-1].node_1.fd_x._ids
        self.n_fd = element_fd.next()                                     # Defines it as the number of freedom_degrees
        global_stiffness_matrix = np.zeros((self.n_fd, self.n_fd),dtype=float)
        for element in self.elements:                                     # Iterate along the elements from the Truss
            fd_ids = [element.node_1.fd_x.id,                             # Matrix with the ids from Element's FreedomDegrees
                      element.node_1.fd_y.id,
                      element.node_2.fd_x.id,
                      element.node_2.fd_y.id]
            for i in range(4):
                for j in range(4):
                    k = element.calc_element_stiffness_item(i,j)          # Calculate the individual item
                    global_stiffness_matrix[fd_ids[i]][fd_ids[j]] += k    # Assign it to the matrix super-position
        return global_stiffness_matrix

    def _gen_boundaries_force_array(self, f_or_d = 1):
        # Method to generates force and boundaries matrix based on FD from nodes
        force_matrix          = []                                        # Array with ordened forces
        boundaries_conditions = []                                        # Array with the boundaries conditions
        n_bc                  = []                                        # Array with the oposite from BC ^
        displacements         = []                                        # Array with displacement matrix
        for node in self.nodes:                                           # Iterates over the nodes
            if not node.fd_x.blocked:                                     # Check the block status of fd
                force_matrix.append(node.fd_x.load)
                n_bc.append(node.fd_x.id)
                displacements.append(node.d_x)
            else:
                boundaries_conditions.append(node.fd_x.id)                # Appends Item if not blocked
            if not node.fd_y.blocked:
                force_matrix.append(node.fd_y.load)
                n_bc.append(node.fd_y.id)
                displacements.append(node.d_y)
            else:
                boundaries_conditions.append(node.fd_y.id)
        if f_or_d == 1: #TODO COMMENT THIS
            return force_matrix,  boundaries_conditions, n_bc             # Return all the force_matrix
        else:
            return displacements, boundaries_conditions, n_bc             # Return all the force_matrix

    def calc_nodes_displacement(self):
        # Method to generate the displacement global matrix
        force_matrix, boundaries_conditions, n_bc = self._gen_boundaries_force_array()
        matrix       = self.global_stiffness_matrix
        matrix       = np.delete(matrix, boundaries_conditions, axis = 0) # Cuts Lines in the boundaries_conditions
        matrix       = np.delete(matrix, boundaries_conditions, axis = 1) # Cuts Columns in the boundaries_conditions
        matrix       = np.linalg.inv(matrix)                              # Invert matrix
        #force_matrix = np.array([[item] for item in force_matrix])        # Make it into a Column matrix
        displacement = np.dot(matrix, force_matrix)                       # Multiply Matrixes
        index = 0
        for n in n_bc:                                                    # Iterates on the nodes
            if n % 2 == 1:
                self.nodes[n / 2].d_y = displacement[index]               # Fill the spots with displacement in Y
            else:
                self.nodes[n / 2].d_x = displacement[index]               # Fill the spots with displacement in X
            index += 1
        return displacement

    def calc_nodes_reaction(self):
        # Method to generate the displacement global matrix
        displacements, boundaries_conditions, n_bc = self._gen_boundaries_force_array(0)
        matrix        = self.global_stiffness_matrix
        matrix        = np.delete(matrix, n_bc, axis = 0)# Cuts Lines in the boundaries_conditions
        matrix        = np.delete(matrix, boundaries_conditions, axis = 1)                 # Cuts Columns in the boundaries_conditions
        displacements = np.array([[item] for item in displacements])      # Make it into a Column matrix
        reaction_matrix  = np.dot(matrix, displacements)                  # Multiply Matrixes
        index = 0
        for n in boundaries_conditions:                                   # Iterates on the nodes
            if n % 2 == 1:
                self.nodes[n / 2].fd_y.reaction = reaction_matrix[index][0]# Fill the spots with displacement in Y
            else:
                self.nodes[n / 2].fd_x.reaction = reaction_matrix[index][0]# Fill the spots with displacement in X
            index += 1
        return reaction_matrix

    def calc_elements_stress(self):
        # Method that calculates and sets stress values for Elements
        for element in self.elements:
            element.calc_element_stress()                                 # Iterates throw the elements and Calculate Stress

    def calc_elements_strain(self):
        # Method that calculates and sets strain values for Elements
        for element in self.elements:
            element.calc_element_strain()                                 # Iterates throw the elements and Calculate Strain
