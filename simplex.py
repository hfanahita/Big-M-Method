import math
import numpy as np
def simplex(m, n, c, A, b, B, x, j_N, j_b):
    B_inverse = np.linalg.inv(B)
    print("Data type of B_inverse:", B_inverse.dtype)
    print("Data type of b:", b.dtype)
    print("B_inverse: ", B_inverse)
    print("b: ", b, )
    b_bar = np.dot(B_inverse, b)
    print("b_bar: ", b_bar)
    print("j_b: ", j_b)
    print("c: ", c)
    c_B = [c[i] for i in j_b]
    print("c_B", c_B)
    zj_cj = np.zeros(n)
    y = np.zeros((m, n))
    theta_k = 0
    for j in range(n):
        if j in j_N:
            y[:, j] = np.dot(B_inverse, A[:, j])
        else:
            y[:, j] = 0
    print("y: ", y)
    for j in range(n):
        if j in j_N:
            print("y_j: ", y[:,j])
            zj_cj[j] = np.dot(c_B, y[:,j]) - c[j]
        else:
            zj_cj[j] = 0
    print("zj_cj: ", zj_cj)
    zk_ck = np.max(zj_cj)
    print("zk_ck: ", zk_ck)
    k = np.argmax(zj_cj)
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
            if minimum > b_bar[i] / y[i, k]:
                minimum = b_bar[i] / y[i, k]
                exiting_index = i
        print("exiting_index: ", exiting_index)
        theta_k = minimum
        print("theta_k: ", theta_k)
        print("j_N: ", j_N)
        for j in range(n):
            print("j: ", j)
            if j == k:
                x[j] = theta_k
                print("x[k]: ", x[j])
            elif j in j_N:
                x[j] = 0
                print(j, "is set to zero")
            else:
                i = j_b.index(j)
                print("i: ", i)
                print("b_bar[i]: ", b_bar[i])
                print("y[i, k]; ", y[i, k])
                x[j] = b_bar[i] - np.dot(y[i, k], theta_k)
                print("x[", j, "]= ", x[j])
            print("x: ", x)
        # j_N = k
        # j_b = entering_index
        index_to_replace = j_N.index(k)
        j_N[index_to_replace] = exiting_index
        index_to_replace = j_b.index(exiting_index)
        j_b[index_to_replace] = k
        B = A[:, j_b]
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
