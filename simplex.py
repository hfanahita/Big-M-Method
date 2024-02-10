import math
import numpy as np
def simplex(m, n, c, A, b, B, x, j_N, j_b):
    vectorized_num_correction = np.vectorize(num_correction)
    B_inverse = vectorized_num_correction(np.linalg.inv(B))
    print("Data type of B_inverse:", B_inverse.dtype)
    print("Data type of b:", b.dtype)
    print("B_inverse: ", B_inverse)
    print("b: ", b, )
    b_bar = vectorized_num_correction(np.dot(B_inverse, b))
    print("b_bar: ", b_bar)
    print("j_b: ", j_b)
    print("c: ", c)
    c_B = [c[i] for i in j_b]
    print("c_B", c_B)
    zj_cj = np.zeros(n)
    y = np.zeros((m, n))
    theta_k = 0
    for j in range(n):
        y[:, j] = vectorized_num_correction(np.dot(B_inverse, A[:, j]))

    print("y: ", y)
    for j in range(n):
        if j in j_N:
            print("y_j: ", y[:,j])
            zj_cj[j] = vectorized_num_correction(np.dot(c_B, y[:,j]) - c[j])
        else:
            zj_cj[j] = 0
    print("zj_cj: ", zj_cj)
    zk_ck = vectorized_num_correction(np.max(zj_cj))
    print("zk_ck: ", zk_ck)
    k = vectorized_num_correction(np.argmax(zj_cj))
    print("k: ", k)
    if zk_ck <= 0:
        return x
    elif (y[:, k] <= 0).all():
        #unbound problem
        return -1
    else:
        minimum = math.inf
        exiting_index = -1
        for i in range(m):
            if y[i, k] > 0:
                if minimum > b_bar[i] / y[i, k]:
                    minimum = vectorized_num_correction(b_bar[i] / y[i, k])
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
                # i = j_b.index(j)
                print("np.where(j_b == int(j))[0]: ", np.where(j_b == int(j)))
                i = np.where(j_b == int(j))[0][0]
                print("i: ", i)
                print("b_bar[i]: ", b_bar[i])
                print("y[i, k]; ", y[i, k])
                x[j] = vectorized_num_correction(b_bar[i] - np.dot(y[i, k], theta_k))
                print("x[", j, "]= ", x[j])
            print("x: ", x)
        print("##################################################################################################")
        exiting_x_index = j_b[exiting_index]
        print("exiting_x_index: ", exiting_x_index)
        j_b[exiting_index] = k
        print("j_b_new: ", j_b)
        index_to_replace = np.where(j_N == int(k))[0][0]
        # index_to_replace = j_N.index(k)
        print("entering: j_N.index(k)", index_to_replace)
        print("j_N[index_to_replace]_before:", j_N[index_to_replace] )
        j_N[index_to_replace] = exiting_x_index
        print("j_N[index_to_replace]_after:", j_N[index_to_replace])
        print("j_N new: ", j_N)
        # index_to_replace = j_b.index(exiting_index)
        # j_b[index_to_replace] = k
        B = A[:, j_b]
        print("B_new: ", B)
        # j_N = sorted(j_N)
        # j_b = sorted(j_b)
        # print("final j_N: ", j_N)
        # print("final j_b: ", j_b)
        return simplex(m, n, c , A, b, B, x, j_N, j_b)


    '''
     B = m*n matrix
     bbar = inverse(B)b
     j_b = []
     j_n = []
     c_B = non-zero elements of c in order
     y_j:
     if j in j_N:
     inverse(B)*a_j
     else
     0
     zj-cj
    if j in j_n:
        = c_B * y_j - c_j
    else
     0

    zk-ck = max(zj-cj)

    if zk-ck<=0:
        return x
    elseif y_k<=0:
        return -1 (as an indicator of unboundness)
    else
        theta_k = min {bbar_i/y_ik}

    '''

def num_correction(num):
    if abs(num) <1e-05:
        return 0
    else:
        return num