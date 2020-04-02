


from bisect import bisect

def longest_increasing_subsequence(X):
  """15.4-6: 在 O(nlgn) 的时间内求解一个序列的最长单调递增子序列"""
  s = [float('inf')] * len(X)
  L = 0  # s 中非 inf 的元素数目
  for i in range(len(X)):
    j = bisect(s, X[i])
    s[j] = X[i]
    if j + 1 > L:
      L = j + 1
  res = [None] * L
  k = len(X)
  s.append(float('inf'))
  for i in reversed(range(L)):
    while k > 0:
      k -= 1
      if s[i+1] >= X[k] >= s[i]:
        res[i] = X[k]
        break
  return res