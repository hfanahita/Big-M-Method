from simplex import *
import numpy as np
def adjust_variables(A):
    # number of rows
    m = A.shape[0]
    # number of columns
    n = A.shape[1]
    e_i = np.zeros((m,1))
    for i in range(m):
        e_i[i,0] = 1
        for j in range(n):
            if A[i,j] == 1:
                if np.array_equal(A[:,j], e_i[:,0]):
                    break
                else:
                    if j < n -1 and 1 in A[i, j+1:]:
                        continue
                    else:
                        #R_i
                        A = np.hstack((A, e_i))
                        break
            else:
                if j < n -1 and 1 in A[i, j+1:]:
                    continue
                else:
                    A = np.hstack((A, e_i))
                    break

        e_i[i,0] = 0
    return A