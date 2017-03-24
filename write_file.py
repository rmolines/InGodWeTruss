# -*- coding: utf-8 -*-
__author__  = "Matheus Marotzke"
__copyright__ = "Copyright 2017, Matheus Marotzke"
__license__ = "GPLv3.0"

class FileWriter:
    """Class used to writes the output into a File from a Truss Object"""

    def __init__(self, file_name):
        self.file_name = file_name    # Name of the output file

    def generate_output_from_truss(self, truss, args):
        with open(self.file_name, 'w') as program_output:
            if args[0]:
                program_output.write("*DISPLACEMENTS\n")
                for node in truss.nodes:
                    program_output.write("{0} {1} {2}\n".format(node.id + 1, node.d_x, node.d_y))
            if args[1]:
                program_output.write("\n*ELEMENT_STRAINS\n")
                for element in truss.elements:
                    program_output.write("{0} {1}\n".format(element.id + 1, element.strain))
            if args[2]:
                program_output.write("\n*ELEMENT_STRESSES\n")
                for element in truss.elements:
                    program_output.write("{0} {1}\n".format(element.id + 1, element.stress))
            if args[3]:
                program_output.write("\n*REACTION_FORCES\n")
                for node in truss.nodes:
                    if node.fd_x.reaction != 0:
                        program_output.write("{0} FX = {1}\n".format(node.id + 1, node.fd_x.reaction))
                    if node.fd_y.reaction != 0:
                        program_output.write("{0} FY = {1}\n".format(node.id + 1, node.fd_y.reaction))
