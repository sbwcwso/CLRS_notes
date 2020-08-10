from .linkednode import LinkedNode


class LinkedStack():
  def __init__(self):
    self.head = None

  def push(self, x):
    x = LinkedNode(x)
    x.next = self.head
    self.head = x

  def pop(self):
    if self.head is None:
      raise Exception("stack underflow")
    x = self.head.key
    self.head = self.head.next
    return x
  
  def is_empty(self):
    return True if self.head is None else False

  def __str__(self):
    if self.head is None:
      return "None"
    x = self.head
    res = ""
    while x.next is not None:
      res += "{} -> ".format(x.key)
      x = x.next
    res += "{} -> None".format(x.key)
    return res