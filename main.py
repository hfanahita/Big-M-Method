import numpy as np
from simplex import *
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
A = np.array([[2.0,1.0,0.0,0.0],[-1.0, 0.0, 1.0, -1.0]])
print(A)

print(adjust_variables(A,m,n))
# x = np.array([0.0,0.0,10.0,3.0,4.0])
# B = [[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]]
# j_N = [0,1]
# j_b = [2,3,4]
# print(simplex(m,n,c,A,b,B,x,j_N,j_b))