def seam_carving(d):
  """思考题 15-8： 基于接链裁剪的图像压缩"""
  m, n = len(d), len(d[0])
  c = [[d[i][j] if i == 0 else 0 for j in range(n)] for i in range(m)]
  for i in range(1, m):
    c[i][0] = min(c[i-1][0], c[i-1][1]) + d[i][0]
    for j in range(1, n-1):
      c[i][j] = min(c[i-1][j-1], c[i-1][j] ,c[i-1][j+1]) + d[i][j]
    c[i][n-1] = min(c[i-1][n-2], c[i-1][n-1]) + d[i][j]
  
  # 重构最优解
  mini_cost, k = float('inf'), None
  for i, item in enumerate(c[m-1]):
    if item < mini_cost:
      mini_cost, k = item, i
  res = [None] * m
  i = m - 1
  res[i] = (m, k+1)  # 储存剪切的位置
  
  for j in reversed(range(m-1)):
    mini_index = k
    if k != 0 and c[j][k-1] < c[j][mini_index]:
      mini_index = k - 1
    if k != n-1 and c[j][k+1] < c[j][mini_index]:
      mini_index = k + 1
    i -= 1
    res[i] = ((j+1, mini_index+1))
    k = mini_index
  return mini_cost, res


if __name__ == "__main__":
  import random

  d = [[random.randint(10, 99) for j in range(8)] for i in range(6)]
  print("破坏度矩阵为：") 
  print("\n".join([str(item) for item in d]))
  mini_cost, res = seam_carving(d)
  print("最小破环度为： ", mini_cost)
  print("裁剪位置为：", res)
  res_sum = sum(d[item[0]-1][item[1]-1] for item in res)
  assert res_sum == mini_cost