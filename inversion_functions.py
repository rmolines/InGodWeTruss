import math
import numpy as np

A = np.array([[10,-1,2,0],[-1,11,-1,3],[2,-1,10,-1],[0,3,-1,8]], dtype=np.float)
b = np.array([[6],[25],[-11],[15]], dtype=np.float)

def gauss_seidel(matrix_a, matrix_b):
    e_p = 10**-6 #permitted error
    e = 0.011
    n = len(matrix_b)
    h = 0
    x = np.array([0]*n, dtype=np.float)
    x_old = np.array([0]*n, dtype=np.float)

    while (e>e_p):
        e = 0
        for i in range(n):
            x[i] = matrix_b[i]/matrix_a[i][i]
            for j in range(n):
                if (j==i):
                    continue
                else:
                    x[i] -= matrix_a[i][j]*x[j]/matrix_a[i][i]
        
        for i in range(n):
            current_e = (x[i]-x_old[i])/x[i]
            if current_e>e:
                e = current_e
            x_old[i] = x[i]
    return x

def jacobi(matrix_a, matrix_b):
    e = 10^15
    n = len(matrix_b)
    x = np.array([0.0]*n)
    x_temp = np.array([0.0]*n)
    polinomial_matrix = np.array([[0.0]*n]*n)
    for g in range(10):
        for i in range(n):
            kth_x = matrix_b[i]/matrix_a[i][i]
            for j in range(n):
                if (j==i):
                    continue
                else:
                    kth_x -= matrix_a[i][j]*x[j]/matrix_a[i][i]
            e = (kth_x-x_temp[i])/kth_x
            x_temp[i] = kth_x
        
        for i in range(n):
            current_e = (x_temp[i]-x[i])/x_temp[i]
            if current_e>e:
                e = current_e
        x = x_temp

    return x
