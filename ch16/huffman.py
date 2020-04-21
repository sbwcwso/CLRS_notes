import heapq

      
class HuffmanNode:
  """赫夫曼编码的结点"""
  def __init__(self, coding=None, freq=None, left=None, right=None, encoding=None):
    self.coding = coding
    self.freq = freq
    self.left = left
    self.right = right
    self.encoding = encoding

  def __lt__(self, other):
    return True if self.freq < other.freq else False
  
  def __repr__(self):
    if self.encoding is None:
      return "HuffmanNode(coding={}, freq={})".format(self.coding, self.freq)
    else:
      return "HuffmanNode(coding={}, freq={}, encoding={})".format(self.coding, self.freq, self.encoding)

  def __str__(self):
    """逆时针旋转 90 度打印树中结点的 freq 属性"""
    def _helper(root, i):
      res = ''
      if root is None:
        return res
      res += _helper(root.right, i+1)
      res += "|  " * i + str(root.freq) + "\n"
      res += _helper(root.left, i+1)
      return res

    return _helper(self, 0)

  def get_encoding(self):
    """为各个叶结点添加编码值"""
    def _helper(root, prefix):
      if root is None:
        return
      if root.left is None and root.right is None:
        root.encoding = prefix
        return
      _helper(root.left, prefix + "0")
      _helper(root.right, prefix + "1")
    
    _helper(self, '')


def huffman(C):
  """"""
  n = len(C)
  Q = list(C)
  heapq.heapify(Q)
  for i in range(n-1):
    z = HuffmanNode()
    z.left = heapq.heappop(Q)
    z.right = heapq.heappop(Q)
    z.freq = z.left.freq + z.right.freq
    heapq.heappush(Q, z)
  return heapq.heappop(Q)