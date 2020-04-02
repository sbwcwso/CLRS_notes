""""支持连续操作的红黑树"""


from ch13.rb_tree import RBTree, RBNode


class RBTreeWithTbh(RBTree):
  """包含黑高属性 (bh) 的红黑树"""
  def __init__(self, keys = None, root = None):
    super().__init__(root=root)
    self.bh = 0
    if keys:
      for key in keys:
        self.insert(RBNode(key=key))
  
  def insert_fixup(self, z):
    """在插入结点的过程中，维护黑高 bh 的性质"""
    while z.parent.color == RBNode.R:
      if z.parent == z.parent.parent.left:
        y = z.parent.parent.right
        if y.color == RBNode.R:  # case 1
          z.parent.color = RBNode.B
          y.color = RBNode.B
          z.parent.parent.color = RBNode.R
          z = z.parent.parent
        else:
          if z.parent.right == z: # case 2
            z = z.parent
            self.left_rotate(z)
          z.parent.color = RBNode.B
          z.parent.parent.color = RBNode.R
          self.right_rotate(z.parent.parent)
      else:
        y = z.parent.parent.left
        if y.color == RBNode.R:  # case 1
          z.parent.color = RBNode.B
          y.color = RBNode.B
          z.parent.parent.color = RBNode.R
          z = z.parent.parent
        else:
          if z.parent.left == z: # case 2
            z = z.parent
            self.right_rotate(z)
          z.parent.color = RBNode.B
          z.parent.parent.color = RBNode.R
          self.left_rotate(z.parent.parent)
    if self.root.color == RBNode.R:       
      self.root.color = RBNode.B
      self.bh +=1

  def delete_fixup(self, x):
    """删除结点时，维护红黑树的 bh 性质"""
    if x == self.root and x.color == RBNode.B:  # x 为根节点且颜色为黑，双重黑色会被消除为单重，黑高减 1
      self.bh -= 1
      return
    while x != self.root and x.color == RBNode.B:
      if x == x.parent.left:
        w = x.parent.right
        if w.color == RBNode.R:  # case 1
          x.parent.color = RBNode.R
          w.color = RBNode.B
          self.left_rotate(x.parent)
          w = x.parent.right  # 让下面的 case 能正常执行
        if w.left.color == RBNode.B and w.right.color == RBNode.B:  # case 2
          w.color = RBNode.R
          x = x.parent
          if x == self.root:  # 额外的黑色上升至根结点，黑高需减 1
            self.bh -= 1
        else:
          if w.right.color == RBNode.B:  # case 3
            w.left.color = RBNode.B
            w.color = RBNode.R
            self.right_rotate(w)
            w = x.parent.right
          # case 4
          w.color = x.parent.color
          x.parent.color = RBNode.B
          w.right.color = RBNode.B
          self.left_rotate(x.parent)
          x = self.root # 让下一次循环退出循环，同时确保根为黑色
      else:
        w = x.parent.left
        if w.color == RBNode.R:  # case 1
          x.parent.color = RBNode.R
          w.color = RBNode.B
          self.right_rotate(x.parent)
          w = x.parent.left  # 让下面的 case 能正常执行
        if w.left.color == RBNode.B and w.right.color == RBNode.B:  # case 2
          w.color = RBNode.R
          x = x.parent
          if x == self.root:
            self.bh -= 1
        else:
          if w.left.color == RBNode.B:  # case 3
            w.right.color = RBNode.B
            w.color = RBNode.R
            self.left_rotate(w)
            w = x.parent.left
          # case 4
          w.color = x.parent.color
          x.parent.color = RBNode.B
          w.left.color = RBNode.B
          self.right_rotate(x.parent)
          x = self.root # 让下一次循环退出循环，同时确保根为黑色
    x.color = RBNode.B #针对红黑色的情况
  
  def verify(self):
    """验证红黑树的黑高是否正确"""
    bh = 0
    x = self.root
    while x != None:
      if x.color == RBNode.B:
        bh += 1
      x = x.left
    assert self.bh == bh, "T.bh is not right!"

  def get_bh_max(self, bh):
    """获取黑高为 bh 的最大的黑色结点"""
    x = self.bh
    y = self.root
    while y != None and x != bh:
      if y.color == RBNode.B:
        x -= 1
      y = y.right
    return y.right if y.color == RBNode.R else y

  def get_bh_min(self, bh):
    """获取高度为 bh 的最小的黑色结点"""
    x = self.bh
    y = self.root
    while y != None and x!=bh:
      if y.color == RBNode.B:
        x -= 1
      y = y.left
    return y if y.color == RBNode.B else y.left


def RB_join(T1, x, T2):
  """T1 中的所有关键字 < x.key < T2 中的所有关键字，返回三者合并后的红黑树 T"""
  T = RBTreeWithTbh()
  if T1.bh > T2.bh:
    T = T1
    y = T1.get_bh_max(T2.bh)
    x.right = T2.root
    T.transplant(y, x)
    x.left = y
    y.parent = x
  elif T1.bh < T2.bh:
    T = T2
    y = T2.get_bh_min(T1.bh)
    x.left = T1.root
    T.transplant(y, x)
    x.right = y
    y.parent = x
  else:
    T.root = x
    x.left = T1.root
    x.right = T2.root
    x.color = RBNode.B
    T.bh = T1.bh + 1
    return T

  x.color = RBNode.R
  T.insert_fixup(x)
  return T