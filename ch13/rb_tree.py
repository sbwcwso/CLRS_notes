"""红黑树的相关类"""

from ch12.binary_search_tree import BinarySearchTree


class RBNode():
  """红黑树的结点"""
  R = False  # 红色结点
  B = True  # 黑色结点

  def __init__(self, left=None, right=None, parent=None, color=R, key=None):
    self.left = left
    self.right = right
    self.parent = parent
    self.color = color
    self.key = key
  
  def __repr__(self):
    key = self.key if self.key is not None else 'None'
    color = 31 if self.color == RBNode.R else 37  # 为了对比明显，用白色表示黑色结点，红色表示红色结点
    return '\033[0;{}m{}\033[0m'.format(color, key)
  
  def __eq__(self, other):
    return self.key == None if other is None else self is other  # 为了兼容二叉搜索树中的相关函数


class RBTree(BinarySearchTree):
  """红黑树"""
  def __init__(self, root = None, keys=None):
    self.NIL = RBNode(color=RBNode.B) # 黑色的 T.Nil 结点
    self.root = root
    if keys:  # 如何 keys 不为空，则将其中的元素插入红黑树中
      for key in keys:
        self.insert(RBNode(key=key))

  def _binary_tree_insert(self, z):
    """普通二叉树插入，不考虑结点的颜色是否符合要求，主要为了直接借助二叉搜索树的相关函数，构造二叉树"""
    super().insert(z)

  def left_rotate(self, x):
    """左旋操作，需要确保 $x.right 存在$"""
    y = x.right
    x.right = y.left
    if y.left != None: # 为了后续顺序统计树的使用，此处用 None 替换 self.NIL
      y.left.parent = x
    y.left = x
    y.parent = x.parent
    y.left = x
    
    if x.parent == None:
      self.root = y
    elif x.parent.left == x:
      x.parent.left = y
    else:
      x.parent.right = y

    x.parent = y

  def right_rotate(self, x):
    """右旋操作，前提是 $x.left$ 存在"""
    y = x.left
    x.left = y.right
    if y.right != None:
      y.right.parent = x
    
    y.parent = x.parent
    y.right = x

    if x.parent == None:
      self.root = y
    elif x.parent.left == x:
      x.parent.left = y
    else:
      x.parent.right = y

    x.parent = y

  def insert(self, z, fix=True):
    """红黑树的插入操作，直接调用二叉树的插入操作即可，不过要将相应的 None 替换为 nil"""
    super().insert(z)
    if self.root == z:
      z.parent = self.NIL
    z.left = self.NIL
    z.right = self.NIL
    z.color = RBNode.R

    if fix:  # 为了方便扩展红黑树
      self.insert_fixup(z)

  def insert_fixup(self, z):
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
        
    self.root.color = RBNode.B

  def transplant(self, u, v):
    if u.parent == None:
      self.root = v
    elif u.parent.left == u:
      u.parent.left = v
    else:
      u.parent.right = v
    v.parent = u.parent

  def delete(self, z, fix=True):
    """删除某个结点，同时根据 fix 的值来确定是否修复红黑树的性质"""
    y = z
    y_original_color = y.color
    if z.left == None:
      x = z.right
      self.transplant(z, z.right)
    elif z.right == None:
      x = z.left
      self.transplant(z, z.left)
    else:
      y = self.minimum(z.right)
      y_original_color = y.color
      x = y.right
      if y.parent == z:
        x.parent = y  # 此时 x 可能为 NIL，所以需要对其 parent 特殊赋值，其它的赋值均在 transplant 中完成
      else:
        self.transplant(y, y.right)
        y.right = z.right
        y.right.parent = y
      self.transplant(z, y)
      y.left = z.left
      y.left.parent = y
      y.color = z.color
    if fix:
      if y_original_color == RBNode.B:
        self.delete_fixup(x)
    else:
      return x, y, y_original_color  # 返回相关的值，方便扩充红黑树时使用

  def delete_fixup(self, x):
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