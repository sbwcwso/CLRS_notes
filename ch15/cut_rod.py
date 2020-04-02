"""钢条切割问题"""

def cut_rod(p, n):
  if n == 0:
    return 0
  q = float('-inf')
  for i in range(1, n+1):
    q = max(q, p[i-1] + cut_rod(p, n-i))
  return q


def memoized_cut_rod(p, n):
  """带备忘发的自顶向下法"""
  r = [float('-inf')] * (n+1)
  return memoized_cut_rod_aux(p, n, r)


def memoized_cut_rod_aux(p, n, r):
  """"带备忘录的自顶向下法的辅助函数"""
  if r[n] >=0:
    return r[n]
  if n == 0:
    q = 0
  else:
    q = float('-inf')
    for i in range(1, n+1):
      q = max(q, p[i-1] + memoized_cut_rod_aux(p, n-i, r))
  r[n] = q
  return q 

def bottom_up_cut_rod(p, n):
  """自底向上法"""
  r = [float('-inf')] * (n + 1)
  r[0] = 0
  for i in range(1, n+1):
    q = float('-inf')
    for j in range(1, i+1):
      q = max(q, p[j-1] + r[i-j])
    r[i] = q
  return r[-1]


def extend_bottom_up_cut_rod(p, n):
  """保存最优切割方案"""
  r = [float('-inf')] * (n+1)  # 存放最优收益
  s = [0] * n  # 保留最佳切割方案
  r[0] = 0
  for i in range(1, n+1):
    for j in range(1, i+1):
      if r[i] < p[j-1] + r[i-j]:
        r[i] = p[j-1] + r[i-j]
        s[i-1] = j
  return r, s


def print_cut_rod(s, n=None):
  """打印出最佳切割方案"""
  n = len(s) - 1 if n == None else n
  while n >= 0:
    print(s[n], end=" ")
    n = n - s[n]


def cut_rod_with_cost(p, n, c):
  """练习题 15.1-3，需要考虑切割成本"""
  r = [float('-inf')] * (n+1)
  s = [0] * n
  r[0] = c  # 避免后续判断是否需要加上切割成本
  for i in range(1, n+1):
    for j in range(1, i+1):
      t = p[j-1] + r[i-j] - c
      if t > r[i]:
        r[i] = t
        s[i-1] = j
  return r, s


def extend_memoized_cut_rod(p, n):
  """返回切割方案的带备忘发的自顶向下法"""
  r = [float('-inf')] * (n+1)
  s = [0] * n
  extend_memoized_cut_rod_aux(p, n, r, s)
  return r, s
  


def extend_memoized_cut_rod_aux(p, n, r, s):
  """"返回切割方案的带备忘录的自顶向下法的辅助函数"""
  if r[n] >=0:
    return r[n]
  if n == 0:
    q = 0
  else:
    q = float('-inf')
    for i in range(1, n+1):
      t = p[i-1] + extend_memoized_cut_rod_aux(p, n-i, r, s)
      if t > q:
        q = t
        s[n-1] = i
  r[n] = q
  return q 