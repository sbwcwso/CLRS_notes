"""思考题15-3 双调欧几里得旅行商问题"""


def bitonic_euclidean_travel(coordinates):
  """应确保 coordinates 的 x 坐标按升序排列"""
  n = len(coordinates)
  p = [[ ((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)**0.5 if i < j else 0
        for j in range(n)]
        for i in range(n)]
  d = [[float('inf') if i == j-1 else 0
        for j in range(n)]
        for i in range(n)]
  d[0][0] = 0
  d[0][1] = p[0][1]
  d[1][1] = 2 * p[0][1]
  k = [[0]*n for i in range(n)]
  k[0][1] = 1
  for j in range(3, n+1):
    for i in range(1, j+1):
      if i == j - 1:
        for u in range(1, j-1):
          t = d[u-1][j-2] + p[u-1][j-1]
          if t < d[i-1][j-1]:
            d[i-1][j-1] = t
            k[i-1][j-1] = u
      elif i != j:
        d[i-1][j-1] = d[i-1][j-2] + p[j-2][j-1]
      else:
        d[i-1][j-1] = d[j-2][j-1] + p[j-2][j-1]
  # 重构解
  first, second = [], []
  i = n-1
  while i > 1:
    u = k[i-1][i]
    first.extend(reversed(range(u+1, i+1)))
    first, second = second, first
    i = u
  first = [coordinates[i-1] for i in first][::-1]
  second = [coordinates[i-1] for i in second][::-1]
  first.insert(0, coordinates[0])
  second.insert(0, coordinates[0])
  first.append(coordinates[-1])
  second.append(coordinates[-1])
  return d[-1][-1], first, second


if __name__ == "__main__":
  coordinates = ((0, 6), (1, 0), (2, 3), (5, 4), (6, 1), (7, 5), (8, 2))
  d, first, second = bitonic_euclidean_travel(coordinates)
  print("最短的双调欧几里得路径为：", d, "第一条路径为：", first, "第二条路径为：", second)