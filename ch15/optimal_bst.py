""""计算最优二叉搜索树"""


def optimal_bst(p, q):
  n = len(p)
  e = [[ q[i-1] if (i-1) == j else float('inf') for i in range(1, n+2)] for j in range(n+1)]
  w = [[ q[i-1] if (i-1) == j else 0 for i in range(1, n+2)] for j in range(n+1)]
  root = [[0] * n for i in range(n)]
  for l in range(1, n+1):
    for i in range(1, n-l+2):
      j = i + l - 1
      w[i-1][j] = w[i-1][j-1] + p[j-1] + q[j]
      for k in range(i, j+1):
        t = e[i-1][k-1] + e[k][j] + w[i-1][j]
        if t < e[i-1][j]:
          e[i-1][j] = t
          root[i-1][j-1] = k
  return e, root


def construct_optimal_bst(root):
  """15.5-1: 构造最优二叉搜索树"""
  m, n = len(root), len(root[0])
  print("k{} 为根".format(root[0][n-1]))
  construct_optimal_bst_aux(root, 1, n)


def construct_optimal_bst_aux(root, i, j):
  """构造最优二叉搜索树的辅助函数"""
  r = root[i-1][j-1]
  if i == j:
    print("d{} 为 k{} 的左孩子".format(r-1, r))
    print("d{} 为 k{} 的右孩子".format(r, r))
    return
  if i == r:
    print("d{} 为 k{} 的左孩子".format(r-1, r-1))
  else:
    print("k{} 为 k{} 的左孩子".format(root[i-1][r-2], r))
    construct_optimal_bst_aux(root, i, r-1)
  if j == r:
    print("d{} 为 d{} 的右孩子".format(r, r))
  else:
    print("k{} 为 k{} 的右孩子".format(root[r][j-1], r))
    construct_optimal_bst_aux(root, r+1, j)


def improved_optimal_bst(p, q):
  """15.5-4: 改进最优二叉搜索树算法"""
  n = len(p)
  e = [[ q[i-1] if (i-1) == j else float('inf') for i in range(1, n+2)] for j in range(n+1)]
  w = [[ q[i-1] if (i-1) == j else 0 for i in range(1, n+2)] for j in range(n+1)]
  root = [[0] * n for i in range(n)]
  for l in range(1, n+1):
    for i in range(1, n-l+2):
      j = i + l - 1
      w[i-1][j] = w[i-1][j-1] + p[j-1] + q[j]
      if i != j:
        r = range(root[i-1][j-2], root[i][j-1])  # 利用相关的结论
      else:
        r = range(i, j+1)
      for k in range(i, j+1):
        t = e[i-1][k-1] + e[k][j] + w[i-1][j]
        if t < e[i-1][j]:
          e[i-1][j] = t
          root[i-1][j-1] = k
      
  return e, root