import numpy as np
from bigM import *
#min cx
#Ax=b
# input : c: one dimensional array, A: m*n matrix, b: one dimensional array

# Number of variables
n = int(input("Please enter the number of variables: "))
# Number of constraints
m = int(input("Please enter the number of the constructive constraints: "))

# Setting coefficients of the objective function
print("Please enter the n coefficients of the objective function: ")
c_input = input().strip()

c_elements = [float(x) for x in c_input.split()]
c = np.array(c_elements, dtype=float)

# Setting b
b_input = input("Enter b").split()
b = np.array([[float(x)] for x in b_input])

print("Enter the elements of the coefficient matrix, row by row:")

# Setting constraints' coefficient matrix aka A
constraints = []
for i in range(m):
    constraints_input = input(f"Enter {n} elements for constraint {i + 1}, separated by spaces: ")
    constraints_elements = [float(x) for x in constraints_input.split()]
    constraints.append(constraints_elements)

A = np.array(constraints, dtype=float)
print("Input:")
print(A)

initial_basis(A,b,c)
