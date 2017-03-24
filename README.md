
# InGodWeTruss
Python Truss problem solving software

Returns values of DISPLACEMENTS, ELEMENT_STRAINS, ELEMENT_STRESSES and REACTION_FORCES

## Usage:
in_god_we_truss.py -i \<inputfile\> -o \<outputfile\>

## Input file model:

```
*COORDINATES
<number_of_items>
<node_index> <x_coor> <y_coor>
...

*ELEMENT_GROUPS
<number_of_items>
<index> <group_index> <element_type>
...

*INCIDENCES
<element_index> <index_node1> <index_node2>
...

*MATERIALS
<number_of_items>
<material_value_1> <material_value_2> <material_value_3>
...

*GEOMETRIC_PROPERTIES
<number_of_items>
<section_area>
...

*BCNODES
<number_of_items>
<node_index> <freedom_degree>
...

*LOADS
<number_of_items>
<node_index> <freedom_degree> <load>
```
### Obs.
For MATERIALS and GEOMETRIC_PROPERTIES the program accepts 'E' as in '2E-4'. Converting it into: '2 * 10⁻⁴'.

<material_value_1> <material_value_2> <material_value_3>, specification will come soon;

<freedom_degree> is indicated by either 1 or 2 representing x and y respectively;

The application still doesn't implement different ELEMENT_GROUPS;

## Specs

This software was developed as part of a Solid Mechanics Discipline assignment

*@ Insper - 2017 - Computer Engineering class*

And It's under GPLv3 License!
