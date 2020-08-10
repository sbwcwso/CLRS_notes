"""16.2-5"""
import random


def get_intervals(points):
  points = sorted(points)
  res = []
  start_point = points[0]
  res.append((start_point, start_point+1))
  for i in range(1, len(points)):
    if points[i] - start_point > 1:
      start_point = points[i]
      res.append((start_point, start_point+1))
  return res


if __name__ == "__main__":
  points = [random.uniform(0, 5) for i in range(5)]
  print("点的集合为： ", points)
  print("结果为：\n", "\n".join(repr(item) for item in get_intervals(points)))