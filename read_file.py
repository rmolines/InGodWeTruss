# -*- coding: utf-8 -*-
__author__  = "Matheus Marotzke"
__copyright__ = "Copyright 2017, Matheus Marotzke"
__license__ = "GPLv3.0"

import math
import numpy as np
from aux_func import *
from element import Element
from freedom_degree import FreedomDegree
from node import Node
from truss import Truss

class FileReader:
    """Class used to read and interpret the File content into creating a Truss Object"""

    node_list = []              # List with all the nodes
    element_list = []           # List with all the elements

    possible_params = {         # Dictionary that associates PARAMs and Functions
    "COORDINATES"          : coordinates,
    "ELEMENT_GROUPS"       : elements,
    "INCIDENCES"           : incidences,
    "MATERIALS"            : materials,
    "GEOMETRIC_PROPERTIES" : geom_properties,
    "BCNODES"              : bc_nodes,
    "LOADS"                : loads
    }

    def __init__(self, file_name):
        self.file_name = file_name    # Name of the input file

    def generate_truss_from_input(self):
        # Reads the input File and generates a Truss with the specifications
        with open(self.file_name, 'r') as user_input:               # Start reading the File
            data = user_input.read().replace("\r\n",",").split('*') # Clears the garbage in the file, stablishing breaks
            param = ''                                              # Set the param variable as ''
            for parameters in data:                                 # Reading the macro data
                for letter in parameters:                           # Reading the micro data
                    if letter == ",":                               # Looking for breaks stablished before
                        break
                    param += letter                                 # Creating the String with PARAM
                if param in self.possible_params.keys():            # Looks for param in the possible_params list
                    self.node_list, self.element_list = self.possible_params[param](parameters.split(','), self.node_list, self.element_list)
                    param = ''
            truss = Truss(self.node_list, self.element_list)        # Generates the Truss with the values
            return truss
