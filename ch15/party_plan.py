from collections import deque


class Node():
  """用来储存职员信息的结点"""
  def __init__(self, name=None, left_child=None, right_sibling=None, parent=None, point=0):
    self.name = name
    self.left_child = left_child
    self.right_sibling = right_sibling
    self.point = point
    self.parent = parent
    self.attend = None
    self.attend_points = None
    self.not_attend_points = None

  def __repr__(self):
    return str(self.name)

def calc_points(root):
  """计算特定结点的 attend_points 和 not_attend_points 属性"""
  if root.attend_points is not None:  # 避免重复计算
    return
  root.attend_points = root.point
  root.not_attend_points = 0
  child = root.left_child
  while child is not None:
    calc_points(child)
    root.attend_points += child.not_attend_points
    root.not_attend_points += max(child.attend_points, child.not_attend_points)
    child = child.right_sibling


def party_plan(root):
  """思考题 15-6 公司聚会计划"""
  calc_points(root)  # 自顶向下计算 attend_points 和 not_attend_points 属性
  # 层级遍历，构造出席人员
  res = []
  if root.attend_points > root.not_attend_points:
    root.attend, max_points = True, root.attend_points 
    res.append(root)
  else:
    root.attend, max_points = False, root.not_attend_points 
  if root.left_child is None:
    return max_points, res

  dq = deque()
  dq.append(root.left_child)
  while len(dq) > 0:
    x = dq.popleft()
    y = x
    while y is not None:
      if y.left_child is not None:
        dq.append(y.left_child)
      if y.parent.attend or y.attend_points < y.not_attend_points:
        y.attend = False
      else:
        y.attend = True
        res.append(y)
      y = y.right_sibling
  return max_points, res