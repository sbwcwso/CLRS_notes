""""矩阵链乘法的动态规划算法"""
def matrix_chain_order(p):
  """计算矩阵链乘法所需要的最少标量乘法"""
  length = len(p) - 1  # 矩阵链中矩阵的个数
  m = [[ 0 for i in range(length)] for j in range(length)]  # 存放 m[i, j] 的最优解
  s = [[ 0 for i in range(length-1)] for j in range(length-1)]  # 存放 m[i, j]（i < j）最优解对应的分割点 k , 其中 m[i, j] 对应的值存放在 s[i, j-1] 中
  for matrix_length in range(2, length+1):
    for i in range(1, length - matrix_length + 2):
      j = i + matrix_length - 1
      m[i-1][j-1] = float('inf')
      for k in range(i, j):
        q = m[i-1][k-1] + m[k][j-1] + p[i-1]*p[k]*p[j]
        if q < m[i-1][j-1]:
          m[i-1][j-1] = q
          s[i-1][j-2] = k
  return m, s

def print_optimal_parents(s, i, j):
  """根据矩阵 s 中的信息，打印出最优化的括号方案"""
  if i == j:
    print("A{}".format(i), end="")
  else:
    print("(", end="")
    print_optimal_parents(s, i, s[i-1][j-2])
    print_optimal_parents(s, s[i-1][j-2]+1, j)
    print(")", end="")


def matrix_chain_multiply(A, s, i, j):
  """计算矩阵链的乘积"""
  if i == j:
    return A[i-1]
  l = matrix_chain_multiply(A, s, i, s[i-1][j-2])
  r = matrix_chain_multiply(A, s, s[i-1][j-2]+1, j)
  return [[ sum([l[i][k] * r[k][j] for k in range(len(l[0]))])  # 计算两个矩阵的乘积
        for j in range(len(r[0]))]
        for i in range(len(l))]