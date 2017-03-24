# -*- coding: utf-8 -*-
__author__  = "Matheus Marotzke"
__copyright__ = "Copyright 2017, Matheus Marotzke"
__license__ = "GPLv3.0"

import sys, getopt
from read_file import FileReader
from write_file import FileWriter

def main(argv):
    inputfile = ''
    outputfile = ''
    value_args = []
    try:
        opts, args = getopt.getopt(argv,"hstdri:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print 'in_god_we_truss.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h' or opt == '--help' or opt == 'help':
            print '\nin_god_we_truss.py -i <inputfile> -o <outputfile>\n'
            print '-i             input file path'
            print '-o             output file path'
            print '-d             flag for DISPLACEMENT'
            print '-s             flag for ELEMENT_STRAINS'
            print '-t             flag for ELEMENT_STRESSES'
            print '-r             flag for REACTION_FORCES\n'
            sys.exit()
        elif opt == '-d' or opt == '-s' or opt == '-t' or opt == '-r':
            value_args.append(opt)
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    if value_args == []:
        value_args_f = [True]*4
    else:
        value_args_f = [False]*4
        for item in value_args:
            if item == '-d':
                value_args_f[0] = True
            elif item == '-s':
                value_args_f[1] = True
            elif item == '-t':
                value_args_f[2] = True
            elif item == '-r':
                value_args_f[3] = True

    truss_main(inputfile, outputfile, value_args_f)

def truss_main(inputfile, outputfile, args):
    file_reader = FileReader(inputfile)
    file_writer = FileWriter(outputfile)
    truss = file_reader.generate_truss_from_input()
    truss.solve()
    file_writer.generate_output_from_truss(truss, args)


if __name__ == "__main__":
    main(sys.argv[1:])
