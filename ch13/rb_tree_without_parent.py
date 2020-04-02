"""没有父节点的红黑树实现"""

from ch13.rb_tree import RBNode, RBTree
import collections


class RBNodeWithoutParent(RBNode):
  def __init__(self, left=None, right=None, color=RBNode.R, key=None):
    self.left = left
    self.right = right
    self.color = color
    self.key = key

class RBTreeWithoutParent(RBTree):
  """没有父指针的红黑树"""
  def __init__(self):
    self.NIL = RBNodeWithoutParent(color=RBNode.B)
    self.root = self.NIL

  def insert(self, z):
    parents = collections.deque()
    parents.append(self.NIL)
    x = self.root
    y = self.NIL
    while x != self.NIL:
      y = x
      parents.append(x)
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
    z.color = RBNode.R
    self.insert_fixup(z, parents)
  
  def insert_fixup(self, z, parents):
    p = parents.pop()
    while p.color == RBNode.R:
      pp = parents.pop()
      if pp.left == p:
        if pp.right.color == RBNode.R:
          pp.left.color = RBNode.B
          pp.right.color = RBNode.B
          pp.color = RBNode.R
          z = pp
          p = parents.pop()
        else:
          if p.right == z:
            self.left_rotate(p, pp)
            z, p = p, z
          ppp = parents.pop()
          p.color = RBNode.B
          pp.color = RBNode.R
          self.right_rotate(pp, ppp)
      else:
        if pp.left.color == RBNode.R:
          pp.left.color = RBNode.B
          pp.right.color = RBNode.B
          pp.color = RBNode.R
          z = pp
          p = parents.pop()
        else:
          if p.left == z:
            self.right_rotate(p, pp)
            z, p = p, z
          ppp = parents.pop()
          p.color = RBNode.B
          pp.color = RBNode.R
          self.left_rotate(pp, ppp)
    self.root.color = RBNode.B

  def left_rotate(self, x, xparent):
    """左旋操作"""
    y = x.right
    x.right = y.left
    y.left = x
    if xparent == None:
      self.root = y
    elif xparent.left == x:
      xparent.left = y
    else:
      xparent.right = y

  def right_rotate(self, x, xparent):
    """右旋操作"""
    y = x.left
    x.left = y.right
    y.right = x
    if xparent == None:
      self.root = y
    elif xparent.left == x:
      xparent.left = y
    else:
      xparent.right = y