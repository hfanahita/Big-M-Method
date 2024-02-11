import numpy
from simplex import *
import numpy as np
def adjust_variables(A):
    # number of rows
    m = A.shape[0]
    # number of columns
    n = A.shape[1]
    # basis variables' index
    j_b = np.zeros(m)
    # number of artificial variables
    num_of_artificial_vars = 0
    e_i = np.zeros((m,1))
    counter = 0
    for i in range(m):
        e_i[i,0] = 1
        for j in range(n):
            if A[i,j] == 1:
                if np.array_equal(A[:,j], e_i[:,0]):
                    j_b[counter] = int(j)
                    print("j_b: ", j_b)
                    counter += 1
                    break
                else:
                    if j < n -1 and 1 in A[i, j+1:]:
                        continue
                    else:
                        #R_i
                        A = np.hstack((A, e_i))
                        j_b[counter] = int(A.shape[1]-1)
                        print("A.shape[1]-1: ", j_b[counter])
                        print("j_b: ", j_b)
                        num_of_artificial_vars += 1
                        counter+=1
                        break
            else:
                if j < n -1 and 1 in A[i, j+1:]:
                    continue
                else:
                    A = np.hstack((A, e_i))
                    j_b[counter] = int(A.shape[1] - 1)
                    print("j_b: ", j_b)
                    counter += 1
                    num_of_artificial_vars += 1
                    break

        e_i[i,0] = 0
        # np.sort(j_b.astype(int))
    return (A,j_b.astype(int),num_of_artificial_vars)
def m_simplex(m, n, c, A, b, B, x, j_N, j_b, artificial_vars_index):
    print("j_b: ", j_b)
    B_inverse = np.linalg.inv(B)
    b_bar = np.dot(B_inverse, b)
    c_B = np.array([(c[int(i),:]) for i in j_b])
    zj_cj = np.zeros((n,2))
    y = np.zeros((m, n))
    theta_k = 0
    for j in range(n):
        y[:, j] = np.dot(B_inverse, A[:, j])

    print("y: ", y)

    for j in range(n):
        if j in j_N:
            print("y_j: ", y[:,j])
            print("multiply(c_B,y[:,j].reshape(-1, 1)) - c[j,:]: ", multiply(c_B,y[:,j].reshape(-1, 1)) - c[j,:])
            zj_cj[j,:] = multiply(c_B,y[:,j].reshape(-1, 1)) - c[j,:]
        else:
            zj_cj[j,:] = np.zeros((1,2))
    print("zj_cj: ", zj_cj)
    zk_ck,k = maximum(zj_cj)
    print("zk_ck: ", zk_ck)
    print("k: ", k)
    # if zk_ck[0] <= 0:
    if first_stop_condition(zj_cj):
        # first stop condition is met
        # if all artificial variables are equal to zero
        if (x[artificial_vars_index] == np.zeros(artificial_vars_index.shape[0])).all():
            # if any of the artificial variables are in j_b then start the process of getting rid of them
            if (np.isin(artificial_vars_index, j_b)).any():
                pass
            else:
                # if all the artificial variables are in j_N then simply remove them from everywhere and continue with normal simplex

                j_N = np.setdiff1d(j_N, artificial_vars_index)
                print("artificial_vars_index: ", artificial_vars_index)
                print("c in simplex: ", c)
                c = convert_back_objective_function_coefficients(c[:-artificial_vars_index.shape[0],:])
                A = A[:,:-artificial_vars_index.shape[0]]
                print("x: ", x)
                x = x[:-artificial_vars_index.shape[0]]
                print("simplex inputs: ", " m: ", m, " n : ", n - artificial_vars_index.shape[0], "\n", "c: ", c , "\n", "A: ", A, "\n","b: ", b, "\n", "B: ", B, "\n", "x: ", x, "\n", "j_N: ", j_N, " j_b", j_b)
                return simplex(m, n - artificial_vars_index.shape[0], c, A, b, B, x, j_N, j_b)
        else:
        #     there is an artificial variable with a positive value in our basis which means that the LP is infeasible
            return -2
        # return x
    elif (y[:, k] <= 0).all():
        #unbound problem
        return -1
    else:
        minimum = math.inf
        exiting_index = -1
        for i in range(m):
            if y[i, k] > 0:
                if minimum > b_bar[i] / y[i, k]:
                    minimum = b_bar[i] / y[i, k]
                    exiting_index = i
                    # r = i
        print("exiting_index: ", exiting_index)
        theta_k = minimum
        print("theta_k: ", theta_k)
        print("j_N: ", j_N)
        # Calculating x_new
        print("##################################################################################################")
        for j in range(n):
            print("j: ", j)
            if j == k:
                print("theta_k: ", theta_k)
                x[j] = theta_k
                print("x[k]: ", x[j])
            elif j in j_N:
                x[j] = 0
                print(j, "is set to zero")
            else:
                print("j_b: ", j_b)
                # i = j_b.index(int(j))
                i = np.where(j_b == int(j))[0][0]
                print("i: ", i)
                print("b_bar[i]: ", b_bar[i])
                print("y[i, k]; ", y[i, k])
                x[j] = b_bar[i] - np.dot(y[i, k], theta_k)
                print("x[", j, "]= ", x[j])
            print("x: ", x)
        print("##################################################################################################")
        exiting_x_index = j_b[exiting_index]
        print("exiting_x_index: ", exiting_x_index)
        j_b[exiting_index] = int(k)
        print("j_b_new: ", j_b)
        index_to_replace = np.where(j_N == int(k))[0][0]
        print("entering: j_N.index(k)", index_to_replace)
        print("j_N[index_to_replace]_before:", j_N[index_to_replace] )
        j_N[index_to_replace] = exiting_x_index
        print("j_N[index_to_replace]_after:", j_N[index_to_replace])
        print("j_N new: ", j_N)
        print("j_b: ", j_b)
        # index_to_replace = j_b.index(exiting_index)
        # j_b[index_to_replace] = k
        B = A[:, j_b]
        print("B_new: ", B)
        # j_N = sorted(j_N)
        # j_b = sorted(j_b)
        # print("final j_N: ", j_N)
        # print("final j_b: ", j_b)
        return m_simplex(m, n, c , A, b, B, x, j_N, j_b, artificial_vars_index)


# a function to multiply an array of arrays to a vertical vector
def multiply(array_of_arrays,b):
    m = array_of_arrays.shape[0]
    sum = np.zeros(m)
    for i in range(m):
        sum = sum + array_of_arrays[i,:]*b[i,:]
    return sum

def maximum(arr):
    n = arr.shape[0]
    max_index = 0
    max_value = arr[0,:]
    for i in range(n):
        if max_value[0] < arr[i,0]:
            max_value = arr[i,:]
            max_index = i
        elif max_value[0] == arr[i,0]:
            if max_value[1] < arr[i, 1]:
                max_value = arr[i,:]
                max_index = i
    return (max_value, max_index)



def adjust_objective_function_coefficients(c, number_of_artificial_variables):
    new_c = np.array([[0, c[0]]])
    for i in range(1,c.shape[0]):
        new_coefficient = np.array([0, c[i]])
        new_c = np.vstack((new_c, new_coefficient))
    for i in range(number_of_artificial_variables):
        new_c = np.vstack((new_c,[1,0]))
    return new_c

def initial_basis(A,b,c):
    m = A.shape[0]
    n = A.shape[1]
    A, j_b, num_of_artificial_vars = adjust_variables(A)
    j_N = np.setdiff1d(np.arange(n), j_b)
    B = numpy.eye(m)
    b_bar = b
    c = adjust_objective_function_coefficients(c, num_of_artificial_vars)
    counter = 0
    x = np.zeros(n+num_of_artificial_vars)
    for i in range(n+num_of_artificial_vars):
        if i in j_b:
            print("counter: ", counter, " b_bar[counter]: ", b_bar[counter])
            x[i] = b_bar[counter]
            counter += 1
    print("m: ", m , " n: ", n+num_of_artificial_vars)
    print("Initial A: \n", A)
    print("j_N: ", j_N)
    print("j_b: ", j_b)
    print("c: ", c)
    print("x: ", x)
    # print()
    print("**************** Simplex: ")
    artificial_vars_index =np.arange(n, n+num_of_artificial_vars)
    print(m_simplex(m,n+num_of_artificial_vars,c,A,b,B,x,j_N,j_b,artificial_vars_index))

def first_stop_condition(zj_cj):
    for row in zj_cj:
        if row[0] > 0:
            return False

    return True

def convert_back_objective_function_coefficients(c):
    c_new = np.zeros(c.shape[0])
    print("c: ", c)
    for i in range(c.shape[0]):
        print("c[i,:]: ", c[i,:])
        c_new[i] = c[i,1]
    return c_new
