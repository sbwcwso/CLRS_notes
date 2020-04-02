"""思考题 15-4 整齐打印"""


def printing_neatly(X, M):
  n = len(X)
  c = [0] * (n+1)
  b = [1] * n
  for j in range(1, n+1):
    c[j] = float('inf')
    blanks = M + 1  # 补上 i == j 时所减去的空格
    for i in reversed(range(1, j+1)):
      blanks -= 1 + len(X[i-1])
      if blanks < 0:
        break
      if j == n:  # 最后一个元素，无需加上最后一行
        if c[j-1] < c[j]:
          b[j-1] = i
          c[j] = c[j-1]
      else:
        t = c[i-1] + blanks ** 3
        if t < c[j]:
          b[j-1] = i
          c[j] = t
  
  # 重构最优解
  last_word = []  # 储存每一行最后一个单词对应的下标
  i = n
  while i > 0:
    last_word.append(i)
    i = b[i-1] - 1
  return c[n], last_word[::-1]


if __name__ == "__main__":
  s = """
  The Zen of Python, by Tim Peters

  Beautiful is better than ugly.
  Explicit is better than implicit.
  Simple is better than complex.
  Complex is better than complicated.
  Flat is better than nested.
  Sparse is better than dense.
  Readability counts.
  Special cases aren't special enough to break the rules.
  Although practicality beats purity.
  Errors should never pass silently.
  Unless explicitly silenced.
  In the face of ambiguity, refuse the temptation to guess.
  There should be one-- and preferably only one --obvious way to do it.
  Although that way may not be obvious at first unless you're Dutch.
  Now is better than never.
  Although never is often better than right now.
  If the implementation is hard to explain, it's a bad idea.
  If the implementation is easy to explain, it may be a good idea.
  Namespaces are one honking great idea -- let's do more of those1G!
  """.split()
  M = 80
  cost, last_word = printing_neatly(s, M)
  print("除最后一行外， 空格数立方的最小值之和为： ", cost)
  print("最终的打印结果为: ")
  print('*'*80)
  for index, item in enumerate(last_word):
    if index == 0:
      print(" ".join(s[:item]).ljust(M, "|"))
    else:
      print(" ".join(s[last_word[index-1]:item]).ljust(M, "|"))