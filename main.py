import numpy as np
from simplex import *
import math
import matplotlib
#min cx
#Ax=b
# input : c: one dimensional array, A: m*n matrix, b: one dimensional array

# n = int(input("Please enter the number of variables: "))
n = 5
# m = int(input("Please enter the number of the constructive constraints: "))
m = 3
# print("Please enter the n coefficients of the objective function: ")
# c = np.array([])
# for i in range(n):
#     x = float(input())
#     c = np.append(c,x)
c = np.array([-2, -6, 0, 0, 0])

# b_input = input("Enter b").split()
# b = np.array([[x] for x in b_input])
b = np.array([[10],[3],[4]])
x = np.zeros(n)

# print("Please enter the coefficient matrix A element by element:")
# A = np.zeros((m,n))
# for i in range(m):
#     for j in range(n):
#         A[i,j] = float(input())
A = np.array([[2,5,1,0,0],[-3, 3, 0, 1, 0],[1,0,0,0,1]])
print(A)

x = np.array([0,0,10,3,4])
B = [[1,0,0],[0,1,0],[0,0,1]]
j_N = [0,1]
j_b = [2,3,4]
print(simplex(m,n,c,A,b,B,x,j_N,j_b))