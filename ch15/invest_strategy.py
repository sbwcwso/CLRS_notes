"""思考题 15-11 库存规划"""
def invertory_plan(d):
  """库存规划
  """
  n, D = len(d), sum(d)
  c = [[ 0 if i == 0 else float('inf')
      for j in range(D+1)]
      for i in range(n+1)]
  b = [[0]*(D+1) for i in range(n+1)]
  w = [0]*(n+1)
  for i in range(1, n+1):
    w[i] = w[i-1] + d[i-1]
    for j in range(D-w[i]+1):
      c[i][j] = c[i-1][0] + product_cost(j+d[i-1]) + invertory_cost(j)
      if i == 1:
        continue
      for k in range(min(D-w[i-1], j+d[i-1])):
        t = c[i-1][k] + product_cost(j-k+d[i-1]) + invertory_cost(j)
        if t < c[i][j]:
          c[i][j] = t
          b[i][j] = k
  # 重构最优生产序列
  res, k = [0] * n, b[n][0]
  res[n-1] = -k+d[n-1]
  for i in reversed(range(i-1)):
    t = b[i+1][k]
    res[i] = k-t+d[i]
    k = t

  return c[n][0], res


def product_cost(x, m=10, c=1000):
  """生产成本`"""
  return 0 if x <=m else (x-m) * c


def invertory_cost(x):
  """存储成本"""
  return 250 * x 


if __name__ == "__main__":
  import random
  d = [random.randint(0, 20) for i in range(11)] + [0]
  m, c = 10, 1000
  cost, res= invertory_plan(d)
  print("m = {}, c = {}".format(m, c))
  print("每件的储存成本为： 250")
  print("每个月销售量为：", d)
  print("*"*60)
  print("每个月的最优生产序列为： ", res)
  print("最低成本为： ", cost)