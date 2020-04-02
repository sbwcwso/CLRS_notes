"""思考题 15-2： 签约棒球自由球员"""


from collections import namedtuple

Player = namedtuple('Player', 'index, cost, VORP')  # 球员属性, cost 的单位为十万


def signing_players(M, X):
  """M 应有 n 行 p 列，分别对应 N 个位置，以及每个位置上有 P 个可选球员"""
  N, P = len(M), len(M[0])
  x = X // 10 ** 5
  c = [[0]*(x+1) for i in range(N+1)]
  d = [[0]*(x+1) for i in range(N+1)]
  
  for i in range(1, N+1):
    for j in range(1, x+1):
      c[i][j] = float('-inf')
      if c[i-1][j] > c[i][j]:
        c[i][j], d[i][j] = c[i-1][j], 0
      for k in range(P):
        remain_money = j - M[i-1][k].cost
        if remain_money < 0:
          continue
        t = c[i-1][remain_money] + M[i-1][k].VORP
        if t > c[i][j]:
          c[i][j], d[i][j] = t, k+1
  
  # 重构最优解
  i, j, res = N, x, []
  while i > 0 and j > 0:
    k = d[i][j]
    if k != 0:
      res.append(M[i-1][k-1])
      i ,j = i-1, j - res[-1].cost
    else:
      i -= 1

  return c[N][x], res[::-1]


if __name__ == "__main__":
  import random
  N, P = 9, 6
  M = [[Player("{}{}".format(i+1, j+1), random.randint(1, 9), random.randint(60, 99)) 
      for j in range(P)]
      for i in range(N)]
  X = 12 * 10 ** 5
  print("球员信息为： \n")
  print("\n".join(str(item) for item in M))
  print("总的招聘费用为：{:.2f} 十万".format(X/10**5))
  print("*"*50)
  cost, res = signing_players(M, 12 * 10 ** 5)
  print("招入的球员为： ")
  print("\n".join(str(item) for item in res))
  print("最大 VORP 值为：", cost)