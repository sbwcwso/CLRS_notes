import numpy as np
import random
import math


def square_matrix_multiply_brute_force(A, B):
    C = [[0 for i in range(len(B[0]))] for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            for k in range(len(A[0])):
                C[i][j] += A[i][k] * B[k][j]
    return C


def square_matrix_multiply_recursive(A, B):
    def _recursive(a_row, a_col, b_row, b_col, size):
        if size == 1:
            return [[A[a_row][a_col] * B[b_row][b_col]]]
        C = [[0 for i in range(size)] for j in range(size)]
        size = size // 2
        A11, A12, A21, A22 = (a_row, a_col), (a_row, a_col + size), \
                             (a_row + size, a_col), (a_row + size, a_col+size)
        B11, B12, B21, B22 = (b_row, b_col), (b_row, b_col + size), \
                             (b_row + size, b_col), (b_row + size, b_col+size)
        # 计算子矩阵相乘的结果
        A11B11 = _recursive(*A11, *B11, size)
        A11B12 = _recursive(*A11, *B12, size)
        A12B21 = _recursive(*A12, *B21, size)
        A12B22 = _recursive(*A12, *B22, size)
        A21B11 = _recursive(*A21, *B11, size)
        A21B12 = _recursive(*A21, *B12, size)
        A22B21 = _recursive(*A22, *B21, size)
        A22B22 = _recursive(*A22, *B22, size)
        # 子矩阵相加得到结果矩阵
        for i in range(size):
            for j in range(size):
                C[i][j]             = A11B11[i][j] + A12B21[i][j]   # C11
                C[i][j + size]      = A11B12[i][j] + A12B22[i][j]   # C12
                C[i+size][j]        = A21B11[i][j] + A22B21[i][j]   # C21
                C[i+size][j+size]   = A21B12[i][j] + A22B22[i][j]   # C22
        return C

    return _recursive(0, 0, 0, 0, len(A))


def square_matrix_multiply_strassen(A, B):
    def _recursive(A, B, a_row, a_col, b_row, b_col, size):
        if size == 1:
            return [[A[a_row][a_col] * B[b_row][b_col]]]
        C = [[0 for i in range(size)] for j in range(size)]
        size = size // 2
        S = [[[0 for k in range(size)] for j in range(size)] for i in range(10)]
        A11, A12, A21, A22 = (a_row, a_col), (a_row, a_col + size), \
                             (a_row + size, a_col), (a_row + size, a_col+size)
        B11, B12, B21, B22 = (b_row, b_col), (b_row, b_col + size), \
                             (b_row + size, b_col), (b_row + size, b_col+size)
        for i in range(size):
            for j in range(size):
                S[0][i][j] = B[i+B12[0]][j+B12[1]] - B[i+B22[0]][j+B22[1]]
                S[1][i][j] = A[i+A11[0]][j+A11[1]] + A[i+A12[0]][j+A12[1]]
                S[2][i][j] = A[i+A21[0]][j+A21[1]] + A[i+A22[0]][j+A22[1]]
                S[3][i][j] = B[i+B21[0]][j+B21[1]] - B[i+B11[0]][j+B11[1]]
                S[4][i][j] = A[i+A11[0]][j+A11[1]] + A[i+A22[0]][j+A22[1]]
                S[5][i][j] = B[i+B11[0]][j+B11[1]] + B[i+B22[0]][j+B22[1]]
                S[6][i][j] = A[i+A12[0]][j+A12[1]] - A[i+A22[0]][j+A22[1]]
                S[7][i][j] = B[i+B21[0]][j+B21[1]] + B[i+B22[0]][j+B22[1]]
                S[8][i][j] = A[i+A11[0]][j+A11[1]] - A[i+A21[0]][j+A21[1]]
                S[9][i][j] = B[i+B11[0]][j+B11[1]] + B[i+B12[0]][j+B12[1]]
        P1 = _recursive(A, S[0], *A11, 0, 0, size)
        P2 = _recursive(S[1], B, 0, 0, *B22, size)
        P3 = _recursive(S[2], B, 0, 0, *B11, size)
        P4 = _recursive(A, S[3], *A22, 0, 0, size)
        P5 = _recursive(S[4], S[5], 0, 0, 0, 0, size)
        P6 = _recursive(S[6], S[7], 0, 0, 0, 0, size)
        P7 = _recursive(S[8], S[9], 0, 0, 0, 0, size)
        # P 矩阵相加得到结果矩阵
        for i in range(size):
            for j in range(size):
                C[i][j]             = P5[i][j] + P4[i][j] - P2[i][j] + P6[i][j]     # C11
                C[i][j + size]      = P1[i][j] + P2[i][j]                           # C12
                C[i+size][j]        = P3[i][j] + P4[i][j]                           # C21
                C[i+size][j+size]   = P5[i][j] + P1[i][j] - P3[i][j] - P7[i][j]     # C22
        return C

    return _recursive(A, B, 0, 0, 0, 0, len(A))


def strassen(A, B):
    """适应方阵长度不为 2 的次幂的情况"""
    m = math.log(len(A), 2)
    size = 2 ** math.ceil(m)
    if size != len(A):
        A1 = [[0 for i in range(size)] for j in range(size)]
        B1 = [[0 for i in range(size)] for j in range(size)]
        C = [[0 for i in range(len(A))] for j in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A)):
                A1[i][j] = A[i][j]
                B1[i][j] = B[i][j]
        C1 = square_matrix_multiply_strassen(A1, B1)
        for i in range(len(A)):
            for j in range(len(A)):
                C[i][j] = C1[i][j]
        return C
    return square_matrix_multiply_strassen(A, B)
        



if __name__ == "__main__":
    A = [[1, 3], [7, 5]]
    B = [[6, 8], [4, 2]]
    print ("A = {}".format(A))
    print ("B = {}".format(B))
    print("The result of square_matrix_multiply_brute_force is:{}".format(square_matrix_multiply_brute_force(A, B)))
    print("The result of square_matrix_multiply_recursive is:{}".format(square_matrix_multiply_recursive(A, B)))
    # print("The result of square_matrix_multiply_strassen is:{}".format(square_matrix_multiply_strassen(A, B)))
    print("The result of numpy.dot is:{}".format(np.dot(A, B)))

    size = 4
    A = [[random.randint(0, 10) for i in range(size)] for j in range(size)]
    B = [[random.randint(0, 10) for i in range(size)] for j in range(size)]
    print ("A = {}".format(A))
    print ("B = {}".format(B))
    print("The result of square_matrix_multiply_brute_force is:{}".format(square_matrix_multiply_brute_force(A, B)))
    print("The result of square_matrix_multiply_recursive is:{}".format(square_matrix_multiply_recursive(A, B)))
    print("The result of square_matrix_multiply_strassen is:{}".format(square_matrix_multiply_strassen(A, B)))
    print("The result of numpy.dot is:{}".format(np.dot(A, B)))

    size = 6
    A = [[random.randint(0, 10) for i in range(size)] for j in range(size)]
    B = [[random.randint(0, 10) for i in range(size)] for j in range(size)]
    print ("A = {}".format(A))
    print ("B = {}".format(B))
    print("The result of strassen is:{}".format(strassen(A, B)))
    print("The result of numpy.dot is:{}".format(np.dot(A, B)))