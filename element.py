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

    ke_model_matrix = np.array([ # Matrix that defines Element's Stiffness
    [ 1, 2, -1, -2],             # 1 = cos²    | -1 = -cos²
    [ 2, 3, -2, -3],             # 2 = cos*sin | -2 = -cos*sin
    [-1,-2,  1,  2],             # 3 = sin²    | -3 = -sin²
    [-2,-3,  2,  3]])

    ke_matrix_values = {         # Matrix that defines values in model_matrix
      1 : cos_squared,
     -1 : cos_squared_neg,
      2 : cos_times_sin,
     -2 : cos_times_sin_neg,
      3 : sin_squared,
     -3 : sin_squared_neg
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
        string = str(self.id) + ': node_1=' + str(self.node_1) + " node_2=" + str(self.node_2)
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
        for i in range(len(ke_model_matrix)):
            for j in range(len(line)):
                k = calc_element_stiffness_item(i, y)
                ke_matrix[i][j] = k
        return ke_matrix

    def calc_element_stiffness_item(self, x, y):
        # Calculate the item for the matrix
        ke_model_matrix[x][y] = model_value              # Finds the value in the model_matrix
        calc_value = ke_matrix_values[model_value]       # Finds the function in the Dictionary
        item  = calc_value(self.cos, self.sin)           # Calls the function and fills the matrix
        item *= ((self.mater * self.area) / self.length) # Times the constant related to the matrix
        return item

    def calc_element_stress(self):
        #TODO : implement funcion
        return
    def calc_element_strain(self):
        #TODO : implement funcion
        return
