"""带有双向链表的顺序统计树"""

from ch14.os_tree import OSTree, OSTreeNode


class OSTreeWithLinkedListNode(OSTreeNode):
  """带有双向链表的顺序统计树结点"""
  def __init__(self, prev=None, next=None, **kwargs):
    super().__init__(**kwargs)
    self.prev = prev
    self.next = next


class OSTreeWithLinkedList(OSTree):
  """带有双向链表的顺序统计树"""
  def __init__(self, root=None):
    self.NIL = OSTreeWithLinkedListNode(key=None, color=OSTreeWithLinkedListNode.B)
    self.NIL.prev = self.NIL
    self.NIL.next = self.NIL
    self.root = self.NIL if root is None else root
  
  def insert(self, z):
    super().insert(z)
    z.next = self.select(self.rank(z) + 1)
    z.prev = z.next.prev
    z.prev.next = z
    z.next.prev = z
  
  def delete(self, z):
    super().delete(z)
    z.next.prev = z.prev
    z.prev.next = z.next
  
  def mini(self):
    return self.NIL.next
  
  def maxi(self):
    return self.NIL.prev

  def successor(self, z):
    return z.next

  def predecessor(self, z):
    return z.prev
  
  def print_linkedlist(self):
    """打印链表"""
    res = 'None ->'
    x = self.NIL.next
    while x != None:
      res += "{} ->".format(x)
      x = x.next
    res += 'None'
    return res


if __name__ == "__main__":
  import random
  ostwll = OSTreeWithLinkedList()
  keys = random.sample(range(100), 10)
  for key in keys:
    ostwll.insert(OSTreeWithLinkedListNode(key=key))
  print('二叉树为：\n{}'.format(ostwll))
  print("双向链表为：{}".format(ostwll.print_linkedlist()))
  print("最大值为：{}".format(ostwll.maxi()))
  print("最小值为：{}".format(ostwll.mini()))
  i = random.choice(keys)
  print("键为 {} 的前驱为:{}".format(i, ostwll.predecessor(ostwll.search(ostwll.root, i))))
  j = random.choice(keys)
  print("键为 {} 的后继为:{}".format(j, ostwll.successor(ostwll.search(ostwll.root, j))))
  print("- "*50)
  print("测试删除结点：")
  random.shuffle(keys)
  for key in keys:
    ostwll.delete(ostwll.search(ostwll.root, key))
    print("- "*50)
    print("删除键 {} 后，二叉树为: \n{}".format(key, ostwll))
    print("双向链表为：{}".format(ostwll.print_linkedlist()))
    print("最大值为：{}".format(ostwll.maxi()))
    print("最小值为：{}".format(ostwll.mini()))