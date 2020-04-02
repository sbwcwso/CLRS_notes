"""持久动态集合"""

from ch12.binary_search_tree import BinarySearchTree


class TreeNodeWithoutParent():
  """没有父结点的结点"""
  def __init__(self, key, left=None, right=None):
    self.key = key
    self.left = left
    self.right = right

  def __repr__(self):
    return str(self.key)


def persistent_tree_insert(root, z):
  """返回插入结点 z 后的新树"""
  if root is None:
    return z
  new_node = TreeNodeWithoutParent(root.key, root.left, root.right)
  if z.key < root.key:
    new_node.left = persistent_tree_insert(root.left, z)
  else:
    new_node.right = persistent_tree_insert(root.right, z)
  return new_node


def print_tree(root):
  """借助二叉搜索树逆时针旋转90度打印一颗树"""
  print(BinarySearchTree(root))


if __name__ == "__main__":
  history = [None]
  root = None
  for i in [4, 2, 5, 1, 6]:
    root = persistent_tree_insert(root, TreeNodeWithoutParent(i))
    history.append(root)
  for root in history:
    print_tree(root)
    print("- "*5)