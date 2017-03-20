# -*- coding: utf-8 -*-
__author__  = "Matheus Marotzke"
__copyright__ = "Copyright 2017, Matheus Marotzke"
__license__ = "GPLv3.0"

import math
import numpy as np
from element import Element
from freedom_degree import FreedomDegree
from node import Node
#from truss import Truss
global possible_params, node_list, element_list
node_list = []
element_list = []

def coordinates(parameters):
    # Function to generate Nodes based on coordinates from file
    for coor in parameters[2::]:                        # Skips ("COORDINATES", # of elements)
        coor = coor.split()                             # Splip them in spaces
        if(len(coor) != 0):                             # Cuts out empthy itens
            fd_x = FreedomDegree(0)
            fd_y = FreedomDegree(1)
            node = Node(float(coor[1]), float(coor[2]), fd_x, fd_y) # Generate node
            node_list.append(node) # Appends Node to the global Node List

def incidences(parameters):
    # Function to generate Elements based on incidences from file, connecting nodes.
    for element in parameters[1::]:                     # Skips ("INCIDENCES")
        element = element.split()                       # Split them in spaces
        if(len(element) != 0):                          # Cuts out empthy itens
            # Get node_1 and node_2 form global node list by id
            node_1  = [node for node in node_list if node.id == int(element[1]) - 1] # Index starts @ 1
            node_2  = [node for node in node_list if node.id == int(element[2]) - 1] # in the File model
            element = Element(node_1[0],node_2[0])      # Generate Element
            element_list.append(element)                # Appends them to the global Element List


def materials(parameters): #TODO - implement the rest of the parameters
    # Function to sets Material values to specific Element
    parameters = parameters[2::]                        # Skips ("MATERIALS", # of elements)
    for i in range(len(parameters)):
        mater  = parameters[i].split()                  # Split them in spaces
        if(len(parameters[i]) > 1):                     # Cuts out empthy itens
        # Calculates the value: '2E-4' -> 2 * 10⁻⁴
            mater                 = mater[0].split('E') # Splits it in the E
            material_value        = float(float(mater[0]) * (10 ** int(mater[1])))
            element_list[i].mater = material_value      # Sets the value into the right Element

def geom_properties(parameters):
    # Function to sets Geometric Property values to specific Element
    parameters = parameters[2::]                        # Skips ("MATERIALS", # of elements)
    for i in range(len(parameters)):
        geom = parameters[i].split("E")                 # Split them in 'E'
        if(len(parameters[i]) > 1):
            # Calculates the value: '2E-4' -> 2 * 10⁻⁴
            geometric_value = float(float(geom[0]) * (10 ** int(geom[1])))
            element_list[i].area = geometric_value      # Sets the value into the right Element

def bc_nodes(parameters):
    # Function to set as blocked specific Freedom Degrees in a Node
    for item in parameters[2::]:                        # Skips ("BCNODES", # of elements)
        item = item.split()                             # Split them in spaces
        if(len(item) != 0):                             # Cuts out empthy itens
            node  = [node for node in node_list if node.id == int(item[0]) - 1] # Index starts @ 1
            if   int(item[1]) == 1:                     # If it's 1 = 'x' = fd_x
                node[0].fd_x.blocked = True             # Set it as blocked
            elif int(item[1]) == 2:                     # If it's 2 = 'y' = fd_y
                node[0].fd_y.blocked = True             # Set it as blocked

def loads(parameters):
    # Function to set load to specific Freedom Degrees in a Node
    for item in parameters[2::]:                        # Skips ("LOADS", # of elements)
        item = item.split()                             # Split them in spaces
        if(len(item) != 0):                             # Cuts out empthy itens
            node  = [node for node in node_list if node.id == int(item[0]) - 1] # Index starts @ 1
            if   int(item[1]) == 1:                     # If it's 1 = 'x' = fd_x
                node[0].fd_x.load = float(item[2])      # Set the load value to the File value
            elif int(item[1]) == 2:                     # If it's 2 = 'y' = fd_y
                node[0].fd_y.load = float(item[2])      # Set the load value to the File value

def elements(parameters):
    return

possible_params = {
"COORDINATES" : coordinates,
"ELEMENT_GROUPS" : elements,
"INCIDENCES" : incidences,
"MATERIALS" : materials,
"GEOMETRIC_PROPERTIES" : geom_properties,
"BCNODES" : bc_nodes,
"LOADS" : loads
}

with open('in.fem', 'r') as user_input:
    data = user_input.read().replace("\r\n",",").split('*')
    param = ''

    for parameters in data:
        for letter in parameters:
            if letter == ",":
                break
            param += letter
        if param in possible_params.keys():
            possible_params[param](parameters.split(','))
            param = ''
