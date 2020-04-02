"""Treap 树"""
from ch12.binary_search_tree import BinaryTreeNode
from ch13.rb_tree import RBTree
import random


class TreapTreeNode(BinaryTreeNode):
  """Treap 树结点"""
  def __init__(self, priority=None, **kwargs):
    super().__init__(**kwargs)
    self.priority = 1/random.random() if priority is None else priority


class TreapTree(RBTree):
  """实现了插入操作的 Treap 树"""
  def __init__(self):
    self.root = None
  
  def insert(self, z):
    """向 treap 树中插入一个元素"""
    x = self.root
    y = None
    while x != None:
      y = x
      if z.key < x.key:
        x = x.left
      else:
        x = x.right
    z.parent = y
    if y == None:
      self.root = z
    elif z.key < y.key:
      y.left = z
    else:
      y.right = z
    
    # 维护 treap 树的性质
    while y != None:
      if y.priority < z.priority:
        return
      if y.left == z:
        self.right_rotate(y)
      else:
        self.left_rotate(y)
      y = z.parent

  def print_priority(self):
    def helper(x, i):
      res = ''
      if x != None:
        res += helper(x.right, i+1)
        res += "\n" + "|    " * i + "{:.2f}\n".format(x.priority)
        res += helper(x.left, i+1)
      return res

    if self.root == None:
      print("None")
    else:
      print(helper(self.root, 0))
  
  def delete(self):
    pass