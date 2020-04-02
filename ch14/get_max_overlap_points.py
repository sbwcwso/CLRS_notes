"""获取最大区间的最大重叠点"""

from ch13.rb_tree import RBNode, RBTree


class RBNodeWithMaxOverlapPoints(RBNode):
  """含有相关附加属性的红黑树结点"""
  def __init__(self, all_sum=None, max_sum=None, point_max=None, point=None,**kwargs):
    self.all_sum = all_sum
    self.max_sum = max_sum
    self.point = point
    self.point_max = point_max
    super().__init__(**kwargs)


class RBTreeWithMaxOverlapPoints(RBTree):
  """含有相关附加属性的红黑树"""
  def __init__(self, keys=None):
    self.NIL = RBNodeWithMaxOverlapPoints(all_sum=0, max_sum=float('-inf'), point_max=None, color = RBNodeWithMaxOverlapPoints.B)
    self.root = self.NIL
    if keys:
      for key in keys:
        self.insert(key)

  @staticmethod
  def update(x):
    """更新结点 x 的相关属性"""
    x.all_sum = x.left.all_sum + x.point + x.right.all_sum
    b = x.left.all_sum + x.point
    c = b + x.right.max_sum
    x.max_sum = max(x.left.max_sum, b, c)
    if x.max_sum == x.left.max_sum:
      x.point_max = x.left.point_max
    elif x.max_sum == b:
      x.point_max = x.key
    else:
      x.point_max = x.right.point_max
    
  def insert(self, z):
    super().insert(z, fix=False)
    z.all_sum = z.point
    z.max_sum = z.point
    z.point_max = z.key
    x = z.parent
    while x != None:
      self.update(x)
      x = x.parent
    self.insert_fixup(z)
  
  def left_rotate(self, z):
    super().left_rotate(z)
    self.update(z)
    self.update(z.parent)

  def right_rotate(self, z):
    super().right_rotate(z)
    self.update(z)
    self.update(z.parent)
  
  def get_max_overlap_points(self):
    return None if self.root == None else self.root.point_max
  

def get_max_overlap_points(intervals):
  """借助扩展的数据结构查找区间的最大重叠点"""
  nodes_left = []
  nodes_right = []
  for interval in intervals:
    nodes_left.append(RBNodeWithMaxOverlapPoints(key=interval[0], point=1))
    nodes_right.append(RBNodeWithMaxOverlapPoints(key=interval[1], point=-1))
  rbt = RBTreeWithMaxOverlapPoints()
  nodes = nodes_left + nodes_right
  for node in nodes:
    rbt.insert(node)
  print("最大重叠点为：", rbt.get_max_overlap_points())
  print("最大重叠的区间数为：", rbt.root.max_sum)


if __name__ == "__main__":
  intervals = [(19, 20), (17, 19), (16, 21), (8, 9), (25, 30), (5, 8), (15, 23), (26, 26), (0, 3), (6, 10)]
  # intervals = [(17, 19), (19, 20)]
  get_max_overlap_points(intervals)