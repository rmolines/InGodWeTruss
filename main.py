# -*- coding: utf-8 -*-
__author__  = "Matheus Marotzke"
__copyright__ = "Copyright 2017, Matheus Marotzke"
__license__ = "GPLv3.0"

from read_file import FileReader

if __name__ == "__main__":
    file_reader = FileReader("in.fem")
    truss = file_reader.generate_truss_from_input()
    print(truss)
