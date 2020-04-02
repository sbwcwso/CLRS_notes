"""顺序统计树"""

from ch13.rb_tree import RBNode, RBTree


class OSTreeNode(RBNode):
  """顺序统计树的结点"""
  def __init__(self, size=0, **kwargs):
    self.size = size
    super().__init__(**kwargs)


class OSTree(RBTree):
  """顺序统计树"""
  def __init__(self, root = None, keys=None):
    self.NIL = OSTreeNode(color=OSTreeNode.B)
    self.root = root if root != None else self.NIL
    if keys:
      for key in keys:
        self.insert(OSTreeNode(key=key))

  def verify(self):
    """验证是否满足顺序统计树的性质"""
    def _helper(x):
      if x != None:
        assert(x.size == x.left.size + x.right.size + 1)
        _helper(x.left)
        _helper(x.right)

    try:
      _helper(self.root)
    except AssertionError:
      raise Exception("Not a order statistics tree!")

  def insert(self, z):
    x = self.root
    y = self.NIL
    while x != self.NIL:
      y = x
      x.size += 1  # 插入路径上的结点 size 加 1
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
    z.size = 1
    z.color = OSTreeNode.R     
    self.insert_fixup(z)

  def left_rotate(self, x):
    super(OSTree, self).left_rotate(x)
    x.parent.size = x.size
    x.size = x.left.size + x.right.size + 1
    
  def right_rotate(self, x):
    super(OSTree, self).right_rotate(x)
    x.parent.size = x.size
    x.size = x.left.size + x.right.size + 1

  def delete(self, z): 
    x, _, y_origin_color = super(OSTree, self).delete(z, fix=False)
    x1 = x
    while x1.parent != None:
      x1 = x1.parent
      x1.size = x1.left.size + x1.right.size + 1
    if y_origin_color == OSTreeNode.B:
      self.delete_fixup(x)

  def select(self, i):
    """返回第 i 个顺序量"""
    def _helper(x, i):
      if x == self.NIL:
        return x
      r =  x.left.size + 1
      if r == i:
        return x
      if r > i:
        return _helper(x.left, i)
      else:
        return _helper(x.right, i-r)
    return _helper(self.root, i)

  def rank(self, x):
    """确定一个元素在中序遍历对应的线性序中的位置""" 
    r = x.left.size + 1
    y = x
    while y != self.root:
      if y.parent.right == y:
        r += y.parent.left.size + 1
      y = y.parent
    return r