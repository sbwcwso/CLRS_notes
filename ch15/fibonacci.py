def fibonacci(n):
  """使用动态规划法计算斐波那契数列"""
  if n == 0: return 0
  if n == 1: return 1
  r = [0] * (n+1)
  r[0], r[1] = 0, 1
  for i in range(2, n+1):
    r[i] = r[i-1] + r[i-2]
  return r[-1]