from simplex import *
import numpy as np
def adjust_variables(A,m,n):
    e_i = np.zeros((m,1))
    e_i_c = np.zeros(m)
    for i in range(m):
        e_i[i,0] = 1
        e_i_c[i] = 1
        print("row: ", i)
        for j in range(n):
            print("j: ", j)
            print("A[i,j]: ", A[i,j])
            if A[i,j] == 1:
                print("A[:,j]: ", A[:,j])
                print("e_i: ", e_i_c)
                if np.array_equal(A[:,j], e_i_c):
                    print("counter + 1 ")
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
        e_i_c[i]=0
    return A