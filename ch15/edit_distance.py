"""思考题15-5 编辑距离"""


def edit_distance(x, y, cost):
  """求最小的编辑距离"""
  m, n = len(x), len(y)
  c = [[float('inf')]*(n+1) for i in range(m+1)]
  d = [[None]*(n+1) for i in range(m+1)]
  # 相关表项的初始化
  c[0][0] = 0
  for i in range(1, m+1):
    c[i][0] = i * cost['delete']
    d[i][0] = 'delete'
  for j in range(1, n+1):
    c[0][j] = j * cost['insert']
    d[0][j] = 'insert'
  for i in range(1, m+1):
    for j in range(1, n+1):
      if x[i-1] == y[j-1]:  # copy
        t = c[i-1][j-1] + cost['copy']
        if t < c[i][j]:
          c[i][j] = t
          d[i][j] = 'copy'
      else:  # replace
        t = c[i-1][j-1] + cost['replace']
        if t < c[i][j]:
          c[i][j] = t
          d[i][j] = 'replace'
      if i >= 2 and j >= 2 and x[i-1] == y[j-2] and x[i-2] == y[j-1]:  # twiddle
        t = c[i-2][j-2] + cost['twiddle']
        if t < c[i][j]:
          c[i][j] = t
          d[i][j] = 'twiddle'
      t = c[i-1][j] + cost['delete']  # delete
      if t < c[i][j]:
        c[i][j] = t
        d[i][j] = 'delete'
      t = c[i][j-1] + cost['insert']  # insert
      if t < c[i][j]:
        c[i][j] = t
        d[i][j] = 'insert'
  kill_index = -1
  for k in range(0, m):  # kill 操作
    t = c[k][n] + cost['kill']
    if t < c[m][n]:
      kill_index = k + 1
      c[m][n] = t
  # 重构最优解
  res = []
  if kill_index == -1:
    i, j = m, n
  else:
    i, j = kill_index, n
    res.append('kill')
  while i > 0 or j > 0:
    if d[i][j] == 'copy':
      res.append('copy {}'.format(x[i-1]))
      i, j = i-1, j-1
    elif d[i][j] == 'replace':
      res.append('replace {} by {}'.format(x[i-1], y[j-1]))
      i, j = i-1, j-1
    elif d[i][j] == 'twiddle':
      res.append('twiddle {} with {}'.format(x[i-1], x[i-2]))
      i, j = i-2, j-2
    elif d[i][j] == 'delete':
      res.append('delete {}'.format(x[i-1]))
      i = i - 1
    elif d[i][j] == 'insert':
      res.append('insert {}'.format(y[j-1]))
      j = j -1
  return c[m][n], res[::-1]


def align_sequences(x, y, cost):
  """借助编辑距离求序列对齐的最佳方案"""
  m, n = len(x), len(y)
  c = [[float('-inf')]*(n+1) for i in range(m+1)]
  d = [[None]*(n+1) for i in range(m+1)]
  # 相关表项的初始化
  c[0][0] = 0
  for i in range(1, m+1):
    c[i][0] = i * cost['delete']
    d[i][0] = 'delete'
  for j in range(1, n+1):
    c[0][j] = j * cost['insert']
    d[0][j] = 'insert'
  for i in range(1, m+1):
    for j in range(1, n+1):
      if x[i-1] == y[j-1]:  # copy
        t = c[i-1][j-1] + cost['copy']
        if t > c[i][j]:
          c[i][j] = t
          d[i][j] = 'copy'
      else:  # replace
        t = c[i-1][j-1] + cost['replace']
        if t > c[i][j]:
          c[i][j] = t
          d[i][j] = 'replace'
      t = c[i-1][j] + cost['delete']  # delete
      if t > c[i][j]:
        c[i][j] = t
        d[i][j] = 'delete'
      t = c[i][j-1] + cost['insert']  # insert
      if t > c[i][j]:
        c[i][j] = t
        d[i][j] = 'insert'
  # 重构最优解
  i, j, x_blanks, y_blanks= m, n, [], []
  while i > 0 or j > 0:
    if d[i][j] == 'copy':
      i, j = i-1, j-1
    elif d[i][j] == 'replace':
      i, j = i-1, j-1
    elif d[i][j] == 'delete':
      y_blanks.append(i-1)
      i = i - 1
    elif d[i][j] == 'insert':
      x_blanks.append(j-1)
      j = j -1
  x_aligned, y_aligned = x, y
  for item in x_blanks:
    x_aligned = x_aligned[:item] + "*" + x_aligned[item:]
  for item in y_blanks:
    y_aligned = y_aligned[:item] + "*" + y_aligned[item:]

  return c[m][n], x_aligned, y_aligned