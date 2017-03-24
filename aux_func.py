# -*- coding: utf-8 -*-
__author__  = "Matheus Marotzke"
__copyright__ = "Copyright 2017, Matheus Marotzke"
__license__ = "GPLv3.0"

################################################################################
""" TRIGONOMETRY """

def sin(y1,y2,dist):
    y_dist = (y2 - y1)
    return float(y_dist/dist)

def cos(x1,x2,dist):
    x_dist = (x2 - x1)
    return float(x_dist/dist)

def cos_pos(cos,sin): return cos

def sin_pos(cos,sin): return sin

def cos_neg(cos,sin): return -cos

def sin_neg(cos,sin): return -sin

def cos_squared(cos,sin): return cos**2

def cos_squared_neg(cos,sin): return -(cos**2)

def cos_times_sin(cos,sin): return cos*sin

def cos_times_sin_neg(cos,sin): return -(cos*sin)

def sin_squared(cos,sin): return sin**2

def sin_squared_neg(cos,sin): return -(sin**2)

################################################################################
""" INPUT INTERPRETATION """

from element import Element
from freedom_degree import FreedomDegree
from node import Node

def coordinates(parameters, node_list, element_list):
    # Function to generate Nodes based on coordinates from file
    for coor in parameters[2::]:                        # Skips ("COORDINATES", # of elements)
        coor = coor.split()                             # Splip them in spaces
        if(len(coor) != 0):                             # Cuts out empthy itens
            fd_x = FreedomDegree(0)
            fd_y = FreedomDegree(1)
            node = Node(float(coor[1]), float(coor[2]), fd_x, fd_y) # Generate node
            node_list.append(node) # Appends Node to the global Node List
    return node_list, element_list

def incidences(parameters, node_list, element_list):
    # Function to generate Elements based on incidences from file, connecting nodes.
    for element in parameters[1::]:                     # Skips ("INCIDENCES")
        element = element.split()                       # Split them in spaces
        if(len(element) != 0):                          # Cuts out empthy itens
            # Get node_1 and node_2 form global node list by id
            node_1  = [node for node in node_list if node.id == int(element[1]) - 1] # Index starts @ 1
            node_2  = [node for node in node_list if node.id == int(element[2]) - 1] # in the File model
            element = Element(node_1[0],node_2[0])      # Generate Element
            element_list.append(element)                # Appends them to the global Element List
    return node_list, element_list

def materials(parameters, node_list, element_list): #TODO - implement the rest of the parameters
    # Function to sets Material values to specific Element
    parameters = parameters[2::]                        # Skips ("MATERIALS", # of elements)
    for i in range(len(parameters)):
        mater  = parameters[i].split()                  # Split them in spaces
        if(len(parameters[i]) > 1):                     # Cuts out empthy itens
            if 'E' in mater[0]:
                # Calculates the value: '2E-4' -> 2 * 10⁻⁴
                mater                 = mater[0].split('E') # Splits it in the E
                material_value        = float(float(mater[0]) * (10 ** int(mater[1])))
            else:
                material_value        = float(mater[0])
            element_list[i].mater     = float(material_value)
    return node_list, element_list

def geom_properties(parameters, node_list, element_list):
    # Function to sets Geometric Property values to specific Element
    parameters = parameters[2::]                        # Skips ("MATERIALS", # of elements)
    for i in range(len(parameters)):
        if(len(parameters[i]) > 1):
            # Calculates the value: '2E-4' -> 2 * 10⁻⁴
            if 'E' in parameters[i]:
                geom = parameters[i].split("E")             # Split them in 'E'
                geometric_value = float(float(geom[0]) * (10 ** int(geom[1])))
            else:
                geom = parameters[i]
            element_list[i].area = geometric_value      # Sets the value into the right Element
    return node_list, element_list

def bc_nodes(parameters, node_list, element_list):
    # Function to set as blocked specific Freedom Degrees in a Node
    for item in parameters[2::]:                        # Skips ("BCNODES", # of elements)
        item = item.split()                             # Split them in spaces
        if(len(item) != 0):                             # Cuts out empthy itens
            node  = [node for node in node_list if node.id == int(item[0]) - 1] # Index starts @ 1
            if   int(item[1]) == 1:                     # If it's 1 = 'x' = fd_x
                node[0].fd_x.blocked = True             # Set it as blocked
            elif int(item[1]) == 2:                     # If it's 2 = 'y' = fd_y
                node[0].fd_y.blocked = True             # Set it as blocked
    return node_list, element_list

def loads(parameters, node_list, element_list):
    # Function to set load to specific Freedom Degrees in a Node
    for item in parameters[2::]:                        # Skips ("LOADS", # of elements)
        item = item.split()                             # Split them in spaces
        if(len(item) != 0):                             # Cuts out empthy itens
            node  = [node for node in node_list if node.id == int(item[0]) - 1] # Index starts @ 1
            if   int(item[1]) == 1:                     # If it's 1 = 'x' = fd_x
                node[0].fd_x.load = float(item[2])      # Set the load value to the File value
            elif int(item[1]) == 2:                     # If it's 2 = 'y' = fd_y
                node[0].fd_y.load = float(item[2])      # Set the load value to the File value
    return node_list, element_list

def elements(parameters, node_list, element_list): #TODO - implement Elements func
    return node_list, element_list

################################################################################
