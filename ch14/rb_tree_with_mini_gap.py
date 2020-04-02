"""带有 mini_gap 属性的红黑树"""

from ch13.rb_tree import RBNode, RBTree


class RBNodeWithMiniGap(RBNode):
  """带有 mini_gap 属性的红黑树结点"""
  def __init__(self, maxi=None, mini=None, mini_gap = None, **kwargs):
    self.maxi = maxi
    self.mini= mini
    self.mini_gap = mini_gap
    super().__init__(**kwargs)
    
    
class RBTreeWithMiniGap(RBTree):
  """带有 mini_gap 属性的红黑树"""
  def __init__(self, root = None, keys=None):
    self.NIL = RBNodeWithMiniGap(maxi=float('-inf'), mini=float('inf'), mini_gap=float('inf'), key=None, color=RBNodeWithMiniGap.B)
    self.root = self.NIL if root == None else root
    if keys:
      for key in keys:
        self.insert(RBNodeWithMiniGap(key=key))

  @staticmethod
  def update(x):
    x.mini = min(x.left.mini, x.key)
    x.maxi = max(x.right.maxi, x.key)
    x.mini_gap = min(x.left.mini_gap, x.right.mini_gap, x.key - x.left.maxi, x.right.mini - x.key)

  def insert(self, z):
    super().insert(z, fix=False)       
    z.maxi = z.key
    z.mini = z.key
    z.mini_gap = float('inf')
    x = z.parent
    while x != None:
      self.update(x)
      x = x.parent
    self.insert_fixup(z)
  
  def delete(self, z):
    x, _, y_origincolor = super().delete(z, fix=False)
    y = x.parent
    while y != None:
      self.update(y)
      y = y.parent
    if y_origincolor == RBNodeWithMiniGap.B:
      self.delete_fixup(x)

  def left_rotate(self, x):
    super().left_rotate(x)
    x.parent.mini = x.mini
    x.parent.maxi = x.maxi
    x.parent.mini_gap = x.mini_gap
    self.update(x)
  
  def right_rotate(self, x):
    super().right_rotate(x)
    x.parent.mini = x.mini
    x.parent.maxi = x.maxi
    x.parent.mini_gap = x.mini_gap
    self.update(x)

  def mini_gap(self):
    return  self.root.mini_gap if self.root.mini_gap != float('inf') else None
    