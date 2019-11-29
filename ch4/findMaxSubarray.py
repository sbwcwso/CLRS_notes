import random


def find_max_subarray_brute_force(A):
    """查找最大子数组的暴力解法"""
    max_sum = -float('inf')
    left, right = 0, 0
    for i in range(len(A)):
        temp_sum = 0
        for j in range(i, len(A)):
            temp_sum += A[j]
            if temp_sum > max_sum:
                max_sum = temp_sum
                left, right = i, j
    return (left, right, max_sum)


def find_max_crossing_subarray(A, low, high):
    if low == high:
        return (low, high, A[low])
    mid = (low + high) // 2
    left_sum_max, left_sum, left = -float('inf'), 0, 0
    for i in reversed(range(low, mid + 1)):
        left_sum += A[i]
        if left_sum > left_sum_max:
            left, left_sum_max = i, left_sum
    right_sum_max, right_sum, right = -float('inf'), 0, 0
    for i in range(mid+1, high+1):
        right_sum += A[i]
        if right_sum > right_sum_max:
            right, right_sum_max = i, right_sum
    return (left, right, left_sum_max + right_sum_max)


def find_max_subarray_recursion(A, low, high):
    """查找最大子数组的递归解法"""
    if low == high:
        return (low, high, A[low])
    mid = (low + high) // 2
    (left_low, left_high, left_max) = find_max_subarray_recursion(A, low, mid)
    (right_low, right_high, right_max) = find_max_subarray_recursion(A, mid + 1, high)
    (mid_low, mid_high, mid_max) = find_max_crossing_subarray(A, low, high)
    if left_max >= right_max and left_max >= mid_max:
        return (left_low, left_high, left_max)
    if right_max >= left_max and right_max >= mid_max:
        return(right_low, right_high, right_max)
    else:
        return(mid_low, mid_high, mid_max)


def find_max_subarray_linear(A):
    """查找最大子数组的线性解法"""
    if len(A) == 1:
        return (0, 0, A[0])
    temp_sum, max_sum = A[0], -float('inf')
    temp_left, left, right = 0, 0, 0
    for i in range(1, len(A)):
        if A[i] > A[i] + temp_sum:
            temp_left = i
            temp_sum = A[i]
        else:
            temp_sum += A[i]
        if temp_sum > max_sum:
            max_sum = temp_sum
            left = temp_left
            right = i
    return (left, right, max_sum)


if __name__ == "__main__":
    # A = [random.randint(-1, 1) for i in range(10)]
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print("A = " + str(A))
    print("The result of brute force is:" + str(find_max_subarray_brute_force(A)))
    print("The result of recursion is:" + str(find_max_subarray_recursion(A, 0, len(A) - 1)))
    A = [random.randint(-5, 5) for i in range(10)]
    print("A = " + str(A))
    print("The result of brute force is:" + str(find_max_subarray_brute_force(A)))
    print("The result of recursion is:" + str(find_max_subarray_recursion(A, 0, len(A) - 1)))
    print("The result of linear is:" + str(find_max_subarray_linear(A)))