"""结点没有父指向父结点的指针，只有指向后继的指针"""
from ch12.binary_search_tree import BinaryTreeNode, BinarySearchTree


class BinaryTreeNodeSuccessor(BinaryTreeNode):
  def __init__(self, left=None, right = None, succ=None, key=None):
    self.left = left
    self.right = right
    self.succ = succ
    self.key = key


class BinarySearchTreeSuccessor(BinarySearchTree):
  def __init__(self, root=None):
    super().__init__(root)

  def search(self, x, k):
    """搜索只需对左右节点进行操作，直接继承即可"""
    return super().search(x, k)

  def parent(self, x):
    if x == self.root:
      return None
    y = self.maximum(x).succ
    if y == None:
      y = self.root
    else:
      if y.left == x:
        return y
      y = y.left
    while y.right != x:
      y = y.right
    return y

  def insert(self, z):
    x = self.root
    y = None
    predecessor = None
    while x != None:
      y = x
      if z.key < x.key:
        x = x.left
      else:
        predecessor = x  # 最后一次转向右子节点的点，一定为最终 y 的前驱
        x = x.right
    if y == None:
      self.root = z
    else:
      if z.key < y.key:
        y.left = z
        z.succ = y
        if predecessor != None:
          predecessor.succ = z 
      else:
        y.right = z
        z.succ = y.succ
        y.succ = z
  
  def predecessor(self, x):
    if x.left != None:
      return self.maximum(x.left)
    y = self.parent(x)
    while y != None and y.left == x:
      x = y
      y = self.parent(y)
    return y

  def transplant(self, u, v):
    u_parent = self.parent(u)
    if u_parent == None:
      self.root = v
    elif u == u_parent.left:
      u_parent.left = v
    else:
      u_parent.right = v
      
  def delete(self, z):
    self.predecessor(z).succ = z.succ
    if z.left == None:
      self.transplant(z, z.right)
    elif z.right == None:
      self.transplant(z, z.left)
    else:
      if z.right != z.succ:
        self.transplant(z.succ, z.succ.right)
        z.succ.right = z.right
      self.transplant(z, z.succ)
      z.succ.left = z.left