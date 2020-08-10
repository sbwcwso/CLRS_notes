"""16.2-2 0-1 背包问题"""

from collections import namedtuple
Item = namedtuple('Item', 'w, v')

def knapsack(items, W):
  n = len(items)
  c = [[0 for j in range(W+1)] for i in range(n+1)]
  d = [[0 for j in range(W+1)] for i in range(n+1)]

  for i in range(1, n+1):
    for j in range(1, W+1):
      c[i][j] = c[i-1][j]
      if j - items[i-1].w >= 0:
        t = c[i-1][j - items[i-1].w] + items[i-1].v
        if t > c[i][j]:
          c[i][j], d[i][j] = t, 1

  # 重构最优解
  res = []
  i, j = n, W
  while i > 0:
    if d[i][j] == 1:
      res.append(items[i-1])
      j = j - items[i-1].w
    i -= 1
  
  return res


if __name__ == "__main__":
  weights = [10, 20, 30]
  values = [60, 100, 120]
  W = 50
  items = []
  for w, v in zip(weights, values):
    items.append(Item(w, v))
  print("所有的商品为：{}".format(items))
  print("背包的容量为：{}".format(W))
  print("结果为：")
  print(knapsack(items, W))