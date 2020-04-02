def string_break(n, L):
  """思考题 15-9 字符串拆分"""
  m = len(L)
  L = [1] + list(L) + [n]
  c = [[L[j]-L[i] + 1 if j == i+2 else 1
      for j in range(m+2)] 
      for i in range(m+2)]
  d = [[i+1 if j == i+2 else None
      for j in range(m+2)] 
      for i in range(m+2)]
  for l in range(4, m+3):
    for i in range(0, m+3-l):
      j = i + l - 1
      c[i][j] = float('inf')
      for k in range(i+1, j):
        t = c[i][k] + c[k][j] + L[j] - L[i]
        if t < c[i][j]:
          c[i][j] = t
          d[i][j] = k

  mini_cost = c[0][m+1]  # 最小代价
  res = []
  construct_break_sequence(L, d, m, res, 0, m+1)
  return mini_cost, res 


def construct_break_sequence(L, d, m, res, i, j):
  """构造最优拆分序列"""
  k = d[i][j]
  res.append(L[k])
  if k > i + 1:
    construct_break_sequence(L, d, m, res, i, k)
  if k < j - 1:
    construct_break_sequence(L, d, m, res, k, j)


if __name__ == "__main__":
  n = 20
  L = [2, 8, 10]
  mini_cost, res = string_break(n, L)
  print("最小拆分代价为：", mini_cost)
  print("对应的拆分序列为：", res)