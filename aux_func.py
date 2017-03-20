# -*- coding: utf-8 -*-
__author__  = "Matheus Marotzke"
__copyright__ = "Copyright 2017, Matheus Marotzke"
__license__ = "GPLv3.0"

def sin(y1,y2,dist):
    y_dist = (y2 - y1)
    return float(y_dist/dist)

def cos(x1,x2,dist):
    x_dist = (x2 - x1)
    return float(x_dist/dist)

def cos_squared(cos,sin): return cos**2

def cos_squared_neg(cos,sin): return -(cos**2)

def cos_times_sin(cos,sin): return cos*sin

def cos_times_sin_neg(cos,sin): return -(cos*sin)

def sin_squared(cos,sin): return sin**2

def sin_squared_neg(cos,sin): return -(sin**2)
