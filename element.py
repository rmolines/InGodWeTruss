# -*- coding: utf-8 -*-
__author__  = "Matheus Marotzke"
__copyright__ = "Copyright 2017, Matheus Marotzke"
__license__ = "GPLv3.0"

import math
import numpy as np
from itertools import count
from aux_func import *

class Element:
    """Class that represents a Bar Element in a Truss"""
    _ids = count(0) # Counts every new object instance

    ke_model_matrix     = np.array([  # Matrix that defines Element's Stiffness
    [ 1, 2, -1, -2],                  # 1 = cos²    | -1 = -cos²
    [ 2, 3, -2, -3],                  # 2 = cos*sin | -2 = -cos*sin
    [-1,-2,  1,  2],                  # 3 = sin²    | -3 = -sin²
    [-2,-3,  2,  3]])

    stress_strain_model = np.array([[ # Matrix that defines Element's for Stain and Stress
     -3, -4, 3, 4]])                  # 3 = cos     |  -3 = -cos
                                      # 4 = sin     |  -4 = -sin

    ke_matrix_values = {              # Matrix that defines values in model_matrix
      1 : cos_squared,
     -1 : cos_squared_neg,
      2 : cos_times_sin,
     -2 : cos_times_sin_neg,
      3 : sin_squared,
     -3 : sin_squared_neg,
      4 : cos_pos,
     -4 : cos_neg,
      5 : sin_pos,
     -5 : sin_neg
      }


    def __init__(self, node_1, node_2, material_value = None, geometric_value = None):
        self.id     = self._ids.next()   # Element's ID
        self.node_1 = node_1             # Elements are connect between 2 obj Node
        self.node_2 = node_2             # Node_1 and node_2
        self.mater  = material_value     # Specific material used
        self.area   = geometric_value    # BAR's section Area
        self.length = self.calc_length() # Indicates the length of a BAR
        self.cos    = cos(self.node_1.x, self.node_2.x, self.length) # Element's angle cos
        self.sin    = sin(self.node_1.y, self.node_2.y, self.length) # Element's andle sin

    def __repr__(self):
        # Method to determine string representation of a Node
        string  = str(self.id) + ': ' + str(self.node_1.id) + "-" + str(self.node_2.id)
        #string += " l:" + str(self.length) + " a:" + str(self.area) # for a more detailed representation
        return string

    def calc_length(self):
        # Calculates the length of the Element
        x_dist = self.node_2.x - self.node_1.x
        y_dist = self.node_2.y - self.node_1.y
        length = float(math.sqrt(x_dist ** 2 + y_dist ** 2))
        return length

    def calc_element_stiffness_matrix(self):
        # Calculates the Stiffness Matrix from the Element
        ke_matrix = np.zeros((4, 4))
        for i in range(len(self.ke_model_matrix)):
            for j in range(len(self.ke_model_matrix[0])):
                k = self.calc_element_stiffness_item(i, j)
                ke_matrix[i][j] = k
        return ke_matrix

    def calc_element_stiffness_item(self, x, y):
        # Calculate the item for the matrix
        model_value = self.ke_model_matrix[x][y]         # Finds the value in the model_matrix
        calc_value = self.ke_matrix_values[model_value]  # Finds the function in the Dictionary
        item  = calc_value(self.cos, self.sin)           # Calls the function and fills the matrix
        item *= ((self.mater * self.area) / self.length) # Times the constant related to the matrix
        return item

    def calc_element_stress(self):
        # Method that calculates the Stress in an Element
        u_matrix = np.array([                            # Array with the FreedomDegrees of an element
        [self.node_1.fd_x.id],
        [self.node_1.fd_y.id],
        [self.node_2.fd_x.id],
        [self.node_2.fd_y.id]])
        for item in self.stress_strain_model[0]:         # Loop through model matrix [-c, -s, c, s]
            calc_item = self.ke_matrix_values[item]      # Function to be Calculated
            item  = calc_item(self.cos, self.sin)        # Calculate the item to each element's cos and sin
            item *= (self.mater / self.length)           # Element's constant value * the item
        self.stress = np.dot(self.stress_strain_model, u_matrix)[0][0] # Multiply the matrixes
        self.stress_strain_model = np.array([[-3, -4, 3, 4]]) # Re-assign the stress_strain_model rvalue
        return self.stress

    def calc_element_strain(self):
        # Method that calculates the Strain in an Element
        u_matrix = np.array([                            # Array with the FreedomDegrees of an element
        [self.node_1.fd_x.id],
        [self.node_1.fd_y.id],
        [self.node_2.fd_x.id],
        [self.node_2.fd_y.id]])
        for item in self.stress_strain_model[0]:         # Loop through model matrix [-c, -s, c, s]
            calc_item = self.ke_matrix_values[item]      # Function to be Calculated
            item  = calc_item(self.cos, self.sin)        # Calculate the item to each element's cos and sin
            item *= (1 / self.length)                    # Element's constant value * the item
        self.strain = np.dot(self.stress_strain_model, u_matrix)[0][0] # Multiply the matrixes
        self.stress_strain_model = np.array([[-3, -4, 3, 4]]) # Re-assign the stress_strain_model rvalue
        return self.strain
