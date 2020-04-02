"""二叉搜索树"""
import random  # 后续删除结点时，可以随机的选择前驱和后继


class BinaryTreeNode():
  """二叉搜索树结点类"""
  def __init__(self, parent=None, left=None, right=None, key=None):
    self.parent = parent
    self.left = left
    self.right = right
    self.key = key
  
  def __repr__(self):
    return 'None' if self.key == None else str(self.key)


class BinarySearchTree():
  """二叉搜索树类"""
  def __init__(self, root=None):
    self.root = root

  def __repr__(self):
    """按逆时针方向旋转 90 度打印二叉树"""
    def helper(x, i):
      res = ''
      if x != None:
        res += helper(x.right, i+1)
        res += "\n" + "|  " * i + "{}\n".format(x)
        res += helper(x.left, i+1)
      return res
    
    return 'None' if self.root == None else helper(self.root, 0)

  def inorder_walker(self, x):
    while x != None:
      self.inorder_walker(x.left)
      print(x.key, end=" ")
      x = x.right  # 尾递归技术

  def preorder_walker(self, x):
    while x != None:
      print(x.key, end=" ")
      self.preorder_walker(x.left)
      x = x.right

  def postorder_walker(self, x):
    if x != None:
      self.postorder_walker(x.left)
      self.postorder_walker(x.right)
      print(x.key, end=" ")

  def search(self, x, k):
    while x != None and k != x.key:
      x = x.left if k < x.key else x.right
    return x

  def minimum(self, x):
    while x.left != None:
      x = x.left
    return x

  def maximum(self, x):
    while x.right != None:
      x = x.right
    return x

  def successor(self, x):
    if x.right != None:
      return self.minimum(x.right)
    y = x.parent
    while y != None and y.right == x:
      x = y
      y = x.parent
    return y

  def predecessor(self, x):
    if x.left != None:
      return self.maximum(x.left)
    y = x.parent
    while y != None and y.left == x:
      x = y
      y = x.parent
    return y

  def insert(self, z):
    x, y = self.root, None
    while x != None:
      y = x
      x = x.left if z.key < x.key else x.right
    z.parent = y
    if y == None:
      self.root = z
    elif z.key < y.key:  # 不能用 y.left 是否为 None 来判断，因为 y 可能为叶子节点
      y.left = z
    else:
      y.right = z


  def transplant(self, u, v):
    if u.parent == None:
      self.root = v
    elif u.parent.left == u:
      u.parent.left = v
    else:
      u.parent.right = v
    if v != None:
      v.parent = u.parent

  def delete(self, z):
    if z.left == None:
      self.transplant(z, z.right)
    elif z.right == None:
      self.transplant(z, z.left)
    else:
      y = self.minimum(z.right)
      if y.parent != z:
        self.transplant(y, y.right)
        y.right = z.right  # 将 y 移动至 z 的位置
        z.right.parent = y
      self.transplant(z, y)
      z.left.parent = y
      y.left = z.left


  def delete_predecessor(self, z):
    """删除时如果左，右子树均存在，则删除前驱而不是后继"""
    if z.left == None:
      self.transplant(z, z.right)
    elif z.right == None:
      self.transplant(z, z.left)
    else:
      y = self.maximum(z.left)
      if y != z.left:
        self.transplant(y, y.left)
        y.left = z.left
        z.left.parent = y
      self.transplant(z, y)
      y.right = z.right
      y.right.parent = y

  def delete_random(self, z):
    if random.randint(0,1) == 0:
      self.delete(z)
    else:
      self.delete_predecessor(z)