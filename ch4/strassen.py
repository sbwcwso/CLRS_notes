import numpy as np
import random


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


if __name__ == "__main__":
    A = [[1, 3], [7, 5]]
    B = [[6, 8], [4, 2]]
    print ("A = {}".format(A))
    print ("B = {}".format(B))
    print("The result of square_matrix_multiply_brute_force is:{}".format(square_matrix_multiply_brute_force(A, B)))
    print("The result of square_matrix_multiply_recursive is:{}".format(square_matrix_multiply_recursive(A, B)))
    print("The result of numpy.dot is:{}".format(np.dot(A, B)))


    A = [[random.randint(0, 10) for i in range(4)] for j in range(4)]
    B = [[random.randint(0, 10) for i in range(4)] for j in range(4)]
    print ("A = {}".format(A))
    print ("B = {}".format(B))
    print("The result of square_matrix_multiply_brute_force is:{}".format(square_matrix_multiply_brute_force(A, B)))
    print("The result of square_matrix_multiply_recursive is:{}".format(square_matrix_multiply_recursive(A, B)))
    print("The result of numpy.dot is:{}".format(np.dot(A, B)))