
from ch14.interval_tree import IntervalTreeNode, IntervalTree
import collections


# x 坐标的命名元组，key 指坐标值， isleft 为 True，表明是矩阵的左边，为 False 表示是矩阵的右边， y_interval 为矩阵对应的 y 轴区间结点
XCoordinate = collections.namedtuple('XCoordinate', ['key', 'is_left', 'y_interval']) 


def get_x_coordinates(rectangle):
  """
  返回矩阵的两个 x 轴坐标
  rectangle = (x1, x2, y1, y2), 其中x1 < x2, y1 < y2
  """
  x1, x2, *y_interval = rectangle
  y_interval = IntervalTreeNode(low=y_interval[0], high=y_interval[1])
  x_low = XCoordinate(x1, True, y_interval)
  x_high = XCoordinate(x2, False, y_interval)
  return x_low, x_high
  

def is_overlap(rectangles):
  """
  检测是否有重合的矩阵
  rectangles 为包含 rectangle 的可迭代对象
  rectangle = (x1, x2, y1, y2), 其中x1 < x2, y1 < y2
  """
  x_list = []
  for rectangle in rectangles:
    x_list.extend(get_x_coordinates(rectangle))
  x_list.sort(key=lambda x: x.key)
  y_interval_tree = IntervalTree()
  for x in x_list:
    if x.is_left:
      if y_interval_tree.search(x.y_interval.int) != None:
        return True
      y_interval_tree.insert(x.y_interval)
    else:
      y_interval_tree.delete(x.y_interval)
  return False


if __name__ == "__main__":
  rectangles = [[2, 5, 7, 44], [50, 53, 3, 82], [67, 84, 17, 62], [22, 38, 42, 50], [5, 7, 90, 95]]
  print("矩阵集合为： ", rectangles)
  if is_overlap(rectangles):
    print("存在重合矩阵")
  else:
    print("不存在重合矩阵")
  print("- "*40)

  rectangles = [[31, 55, 19, 87], [17, 53, 98, 99], [34, 49, 11, 18], [9, 38, 22, 76], [77, 97, 81, 94]]
  print("矩阵集合为： ", rectangles)
  if is_overlap(rectangles):
    print("存在重合矩阵")
  else:
    print("不存在重合矩阵")