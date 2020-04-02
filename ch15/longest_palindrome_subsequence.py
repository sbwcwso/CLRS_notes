"""15-2 最长回文子序列"""


def longest_palindrome_subsequence(X):
  """空间复杂度为 O(n^3)"""
  n = len(X)
  c = [['' if i!=j else X[i] for j in range(n)] for i in range(n)]
  for l in range(2, n+1):
    for i in range(1, n-l+2):
      j = i + l - 1
      if X[i-1] == X[j-1]:
        c[i-1][j-1] = X[i-1] + c[i][j-2] + X[j-1]
      else:
        c[i-1][j-1] = c[i][j-1] if len(c[i][j-1]) > len(c[i-1][j-2]) else c[i-1][j-2]
  return c[0][n-1]


def improved_longest_palindrome_subsequence(X):
  """空间复杂度为 O(n^2)"""
  n = len(X)
  c = [[0 if i!=j else 1 for j in range(n)] for i in range(n)]

  # 计算 c 的值
  for l in range(2, n+1):
    for i in range(1, n-l+2):
      j = i + l - 1
      if X[i-1] == X[j-1]:
        c[i-1][j-1] = c[i][j-2] + 2
      else:
        c[i-1][j-1] = max(c[i][j-1], c[i-1][j-2])

  # 重构最长的回文子序列
  i, j = 1, n
  res = ''
  while i < j:
    if X[i-1] == X[j-1]:
      res = X[i-1] + res
      i += 1
      j -= 1
    elif c[i][j-1] > c[i-1][j-2]:
      i += 1
    else:
      j -= 1
  return res[::-1] + X[i-1] + res if i == j else res[::-1] + res