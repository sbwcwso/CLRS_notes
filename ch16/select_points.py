"""16.2-3 补水点问题"""


def select_points(points, m):
  start_point = 0
  i = 0
  res = []
  while i < len(points):
    if points[i] - start_point > m:
      res.append(points[i-1])
      i -= 1
      start_point = points[i]
    i += 1
  return res


if __name__ == "__main__":
  import random
  distance, m = 25, 5
  points = []
  point = random.randint(1, m)
  while point < distance:
    points.append(point)
    point += random.randint(1, m)
  print("总距离为：{}, 补水间隔 m 为: {}， 所有补水点为：{}".format(distance, m, points))
  
  print("选择的补水点为：")
  print(select_points(points, m))