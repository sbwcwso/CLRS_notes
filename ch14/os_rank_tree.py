""""""
from ch13.rb_tree import RBNode, RBTree


class OSRankTreeNode(RBNode):
  def __init__(self, rank=0, **kwargs):
    """额外含有 rank 属性的红黑树结点"""
    self.rank = rank
    super().__init__(**kwargs)
    
class OSRankTree(RBTree):
  """额外信息为结点在子树中的秩的顺序统计树"""
  def __init__(self, root=None):
    self.NIL = OSRankTreeNode(rank=0, key=None, color=OSRankTreeNode.B)
    self.root = self.NIL if root is None else root

  def left_rotate(self, x):
    """"""
    super().left_rotate(x)   
    x.parent.rank += x.rank
  
  def right_rotate(self, x):
    """"""
    super().right_rotate(x)
    x.rank -= x.parent.rank

  def insert(self, z):
    """"""
    y = self.NIL
    x = self.root
    while x != None:
      y = x
      if z.key < x.key:
        x.rank += 1
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
    z.left = self.NIL
    z.right = self.NIL
    z.rank = 1
    z.color = OSRankTreeNode.R
    self.insert_fixup(z)

  def delete(self, z):
    """"""
    x, y, y_origin_color = super().delete(z, fix=False)
      
    x1 = x
    while x1.parent != None:
      if z.key < x1.parent.key:  # 用 key 进行判断，避免边界情况出问题
        x1.parent.rank -= 1
      x1 = x1.parent
    if y != z:  # 需要放在后面运行，防止上面的 while 循环的修改
      y.rank = z.rank
    if y_origin_color == OSRankTreeNode.B:
      self.delete_fixup(x)
  
  def verify(self):
    """验证 rank 属性是否满足要求"""
    def size(root):
      """统计一棵树的大小"""
      if root == None:
        return 0
      return 1 + size(root.left) + size(root.right)
    
    def helper(root):
      """辅助函数"""
      if root == None:
        return
      left_size = size(root.left)
      try:
        assert(root.rank == left_size + 1)
      except AssertionError:
        raise Exception("Not an OSRankTree!")
      helper(root.left)
      helper(root.right)

    helper(self.root)