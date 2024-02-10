import numpy as np
# from simplex import *
from bigM import *
import math
import matplotlib
#min cx
#Ax=b
# input : c: one dimensional array, A: m*n matrix, b: one dimensional array

# n = int(input("Please enter the number of variables: "))
n = 4
# m = int(input("Please enter the number of the constructive constraints: "))
m = 2
# print("Please enter the n coefficients of the objective function: ")
# c = np.array([])
# for i in range(n):
#     x = float(input())
#     c = np.append(c,x)
# c = np.array([-2, -6, 0, 0, 0])

# b_input = input("Enter b").split()
# b = np.array([[x] for x in b_input])
# b = np.array([[10],[3],[4]])
# x = np.zeros(n)
# A = np.array([[0.0,1.0,1.0,1.0],[1.0, 0.0, 0.0, 0.0],[0.0,1.0,1.0,1.0],[0.0,1.0,1.0,1.0]])

# A = np.array([[5.0,1.0,0.0],[1.0, 0.0, 0.0],[0.0,0.0,1.0]])
A =np.array([[2,1,-1,0], [1,3,0,-1]])
b = np.array([2,3])
print(A)
c = np.array([1,3,0,0])
initial_basis(A,b,c)
# A, j_b, num_of_artificial_vars = adjust_variables(A)
# n_artificial_vars = adjust_variables(A)[1].shape[0]
# print(adjust_objective_function_coefficients(c, n_artificial_vars))
# print(adjust_variables(A)[1].shape[0])
# x = np.array([0.0,0.0,10.0,3.0,4.0])
# B = [[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]]
# j_N = [0,1]
# j_b = [2,3,4]
# print(simplex(m,n,c,A,b,B,x,j_N,j_b))