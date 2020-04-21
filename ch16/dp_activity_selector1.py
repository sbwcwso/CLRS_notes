"""16.1-5 活动选择问题变形"""
from collections import namedtuple

Activity = namedtuple('Activity', 's, f, v')

def dp_activity_selector(activities):
  """活动选择的动态规划算法"""
  activities = [Activity(0, 0, 0)] + activities + [Activity(float('inf'), float('inf'), 0)]
  n = len(activities)
  c = [[ 0 for j in range(n)] for i in range(n)]
  d = [[ 0 for j in range(n)] for i in range(n)]

  for l in range(3, n+1):  # l 为 j - i + 1 的值
    for i in range(0, n-l+1):
      j = l + i - 1
      S_ij = calc_s(activities, i, j)
      if S_ij:
        for k in S_ij:
          t = c[i][k] + c[k][j] + activities[k].v     
          if t > c[i][j]:
            c[i][j], d[i][j] = t, k
  
  return construct_selector(activities, d, 0, n-1)
  

def construct_selector(activities, d, i, j):
  k = d[i][j]
  if k == 0:
    return []
  else:
    return construct_selector(activities, d, i, k) + [activities[k]] + construct_selector(activities, d, k, j)


def calc_s(activities, i, j):
  """返回 S_ij 中所有活动的下标"""
  res = []
  for k in range(i+1, j):
    if activities[k].s >= activities[i].f and activities[k].f <= activities[j].s:
      res.append(k)
  return res