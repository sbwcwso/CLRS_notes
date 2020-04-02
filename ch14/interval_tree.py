"""区间树"""
from ch13.rb_tree import RBNode, RBTree
import collections


Interval = collections.namedtuple('Interval', ['low', 'high'])  # 区间类


class IntervalTreeNode(RBNode):
  def __init__(self, low=None, high=None, maxi=None, **kwargs):
    super().__init__(**kwargs)
    self.int = Interval(low, high)
    self.key = self.int.low
    self.maxi = maxi


class IntervalTree(RBTree):
  """区间树"""
  def __init__(self, intervals=None):
    self.NIL = IntervalTreeNode(maxi=float('-inf'),color=IntervalTreeNode.B)
    self.root = self.NIL
    if intervals:
      for interval in intervals:
        self.insert(IntervalTreeNode(low=interval[0], high=interval[1]))
  
  def insert(self, z):
    x = self.root
    y = self.NIL
    while x != self.NIL:
      y = x
      x.maxi = max(x.maxi, z.int.high)
      if z.key < x.key:
        x = x.left
      else:
        x = x.right
    
    z.parent = y
    if y == self.NIL:
      self.root = z
    elif z.key < y.key:
      y.left = z
    else:
      y.right = z
    z.left = self.NIL
    z.right = self.NIL
    z.maxi = z.int.high
    z.color = IntervalTreeNode.R
    self.insert_fixup(z)

  def delete(self, z):
    """在区间树中删除结点 z"""
    x, _, y_origin_color = super().delete(z, fix=False)
    x1 = x
    while x1.parent != None:
      x1 = x1.parent
      x1.maxi = max(x1.int.high, x1.left.maxi, x1.right.maxi)
      
    if y_origin_color == IntervalTreeNode.B:
      self.delete_fixup(x)
  
  def verify(self):
    """验证是 maxi 属性是否符合区间树的要求"""
    def _helper(root):
      if root != None:
        assert( root.maxi == max(root.int.high, root.left.maxi, root.right.maxi))
        _helper(root.left)
        _helper(root.right)
    try:
      _helper(self.root)
    except AssertionError:
      raise Exception("Not a interval tree!")

  def left_rotate(self, x):
    super().left_rotate(x)
    x.parent.maxi = x.maxi
    x.maxi = max(x.left.maxi, x.right.maxi, x.int.high)


  def right_rotate(self, x):
    super().right_rotate(x)
    x.parent.maxi = x.maxi
    x.maxi = max(x.left.maxi, x.right.maxi, x.int.high)

  def search(self, i):
    """返回一个与 i 重叠的区间，如果没有，则返回 NIL"""
    x = self.root
    while x != self.NIL and (i.low > x.int.high or x.int.low > i.high):
      x = x.left if x.left != self.NIL and i.low <= x.left.maxi else x.right
    return x

  def search_minimum(self, i):
    """返回与 i 重叠的，具有最小低端点的区间"""
    x = self.root
    res = self.NIL
    while x != None:
      if x.int.low <= i.high and i.low <= x.int.high:
        res = x
        x = x.left
        continue
      x = x.left if x.left != None and x.left.maxi <= i.low else x.right
    
    return res

  def search_all(self, i):
    def _helper(x, i):
      if x == None:
        return
      if i.low <= x.int.high and x.int.low <= i.high:
        print(x.int)
      if x.left != None and x.left.maxi >= i.low:
        _helper(x.left, i)
      if x.right != None and x.right.maxi >= i.low and x.int.low <= i.high:
        _helper(x.right, i)

    _helper(self.root, i)

  def search_excatly(self, i):
    """查找区间完全相同的结点"""
    def helper(x, i):
      res = None
      if x.left != None and i.low < x.key and x.left.maxi >= i.high:
        return helper(x.left, i)
      if x.right != None and i.low > x.key and x.right.maxi >= i.high:
        return helper(x.right, i)
      if i.low == x.key:
        if i.high == x.int.high:
          return x
        if x.left != None and x.left.maxi >= i.high:
          res = helper(x.left, i)
        if res != None:
          return res
        elif x.right != None and x.right.maxi >= i.high:
          res = helper(x.right, i)
      return res

    return None if self.root == None else helper(self.root, i)