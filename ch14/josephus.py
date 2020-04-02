"""输出 josephus 排列"""

import collections
from ch14.os_tree import OSTree, OSTreeNode


def josephus_deque(n, m):
  """借助队列求解 josephus 排列"""
  dq = collections.deque(range(1, n+1))
  res = []
  while len(dq) > 0:
    dq.rotate(-(m-1))
    res.append(dq.popleft())
  return res


def josephus_ostree(n, m):
  """借助顺序统树计算 josephus 排列"""
  ostree = OSTree(keys=range(1, n+1))
  size = n
  index = 0
  res = []
  while size > 0:
    index = (index + m) % (size)
    if index == 0:
      index = size
    target = ostree.select(index)
    ostree.delete(target)
    res.append(target.key)
    size -= 1
    index -= 1
  return res