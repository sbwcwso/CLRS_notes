"""AVL 树"""

from ch12.binary_search_tree import BinaryTreeNode
from ch13.rb_tree import RBTree


class AVLTreeNode(BinaryTreeNode):
  """AVL 树结点"""
  def __init__(self, h=0, **kwargs):
    super().__init__(**kwargs)
    self.h = h
  
  def __eq__(self, other):
    return self.key == None if other is None else self is other  # 为了兼容二叉搜索树中的相关函数


class AVLTree(RBTree):
  """实现 avl 树折插入操作"""
  def __init__(self):
    self.NIL = AVLTreeNode(h=-1)
    self.root = self.NIL
  
  def left_rotate(self, x):
    """旋转后需要更新相应结点的高度"""
    super().left_rotate(x)   
    x.h = max(x.left.h, x.right.h) + 1
    x.parent.h = max(x.parent.left.h, x.parent.right.h) + 1
    return x.parent

  def right_rotate(self, x):
    """旋转后需要更新相应结点的高度"""
    super().left_rotate(x)   
    super().right_rotate(x)   
    x.h = max(x.left.h, x.right.h) + 1
    x.parent.h = max(x.parent.left.h, x.parent.right.h) + 1
    return x.parent

  def balance(self, x):
    """平衡 avl 树"""
    if abs(x.left.h - x.right.h) <= 1:
      return x
    if x.left.h > x.right.h:
      if x.left.left.h < x.left.right.h:
        self.left_rotate(x.left)
      return self.right_rotate(x)
    else:
      if x.right.right.h < x.right.left.h:
        self.right_rotate(x.right)
      return self.left_rotate(x)
  
  def delete(self, z):
    """"""
    pass
    

  def insert(self, z):
    def helper(root, z):
      if root == self.NIL:
        z.left = self.NIL
        z.right = self.NIL
        z.parent = self.NIL
        return z
      if z.key < root.key:
        y = helper(root.left, z)
        root.left = y
        y.parent = root
        root.h = y.h + 1
      else:
        y = helper(root.right, z)
        root.right = y
        y.parent = root
        root.h = y.h + 1
      return self.balance(root)
    self.root = helper(self.root, z)