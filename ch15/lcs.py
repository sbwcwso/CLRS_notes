"""最长公共子序列问题"""


def lcs_length(X, Y):
  """求两个序列的最长公共子序列"""
  m, n = len(X), len(Y)
  c = [[0]*(n+1) for i in range(m+1)]
  b = [[None]*n for i in range(m)]
  for i in range(1, m+1):
    for j in range(1, n+1):
      if X[i-1] == Y[j-1]:
        c[i][j] = c[i-1][j-1] + 1
        b[i-1][j-1] = '↖'
      elif c[i-1][j] >= c[i][j-1]:
        c[i][j] = c[i-1][j]
        b[i-1][j-1] = '↑'
      else:
        c[i][j] = c[i][j-1]
        b[i-1][j-1] = '←'
  return c, b

def print_LCS(b, X, i, j):
  """打印出最长公共子序列"""
  if i == 0 or j == 0:
    return
  if b[i-1][j-1] == '↖':
    print_LCS(b, X, i-1, j-1)
    print(X[i-1], end=" ")
  elif b[i-1][j-1] == '↑':
    print_LCS(b, X, i-1, j)
  else:
    print_LCS(b, X, i, j-1)


def print_LCS_without_b(c, X, Y, i, j):
  """15.4-2: 在没有表 b 的情况下输出最长公共子序列"""
  if i == 0 or j == 0:
    return
  if c[i][j] == c[i-1][j-1] + 1:
    print_LCS_without_b(c, X, Y, i-1, j-1)
    print(X[i-1], end=' ')
  elif c[i][j] == c[i-1][j]:
    print_LCS_without_b(c, X, Y, i-1, j)
  else:
    print_LCS_without_b(c, X, Y, i, j-1)


def memoized_lcs_length(X, Y):
  """15.4-3: 带备忘的 lcs 算法"""
  m, n = len(X), len(Y)
  c = [[None] * (n+1) for i in range(m+1)]
  b = [[None]* n for i in range(m)]
  memoized_lcs_length_aux(X, Y, len(X), len(Y), c, b)
  return c, b


def memoized_lcs_length_aux(X, Y, i, j, c, b):
  """带备忘的 lcs 算法的辅助函数"""
  if i == 0 or j == 0:
    return 0
  if X[i-1] == Y[j-1]:
    c[i][j] = 1 + memoized_lcs_length_aux(X, Y, i-1, j-1, c, b)
    b[i-1][j-1] = '↖'
  else:
    up = memoized_lcs_length_aux(X, Y, i-1, j, c, b)
    left = memoized_lcs_length_aux(X, Y, i, j-1, c, b)
    b[i-1][j-1], c[i][j] = ('↑', up) if up >= left else ('←', left)
  return c[i][j]


from collections import deque


def lcs_length_queue(X, Y):
  """15.4-4: 借助队列来减小表项所需的额外空间"""
  m, n = len(X), len(Y)
  if m < n:
    m, n = n, m
    X, Y = Y, X
  dq = deque(maxlen=n)
  a = 0  # 初始时的 c[i-1][j-1]
  for i in range(m):
    for j in range(n):
      if X[i] == Y[j]:
        b = a + 1  if j != 0 else 1 # b 为 c[i][j]
        a = dq.popleft() if i != 0 else 0 # 下一次循环时的 c[i-1][j-1]
        dq.append(b)
      else:
        a = dq.popleft() if i != 0 else 0 # 此次循环的 c[i-1][j], 下一次循环的 c[i-1][j-1]
        d = dq[-1] if j != 0 else 0 # c[i][j-1]
        dq.append(max(a, d))
  return dq[-1]


def longest_increasing_subsequence_by_LCS(X):
  """15.4-5: 在 O(n^2) 的时间内求一个序列的最长单调递增子序列"""
  Y = sorted(X)  
  c, b = memoized_lcs_length(X, Y)
  print_LCS(b, X, len(X), len(Y))