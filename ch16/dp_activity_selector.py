from ch16.activity_selector import Activity
def dp_activity_selector(activities):
  """活动选择的动态规划算法"""
  activities = [Activity(0, 0)] + activities + [Activity(float('inf'), float('inf'))]
  n = len(activities)
  c = [[ 0 for j in range(n)] for i in range(n)]
  d = [[ 0 for j in range(n)] for i in range(n)]

  for l in range(3, n+1):  # l 为 j - i + 1 的值
    for i in range(0, n-l+1):
      j = l + i - 1
      S_ij = calc_s(activities, i, j)
      if S_ij:
        for k in S_ij:
          t = c[i][k] + c[k][j] + 1     
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


if __name__ == "__main__":
  s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
  f = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
  activities = []
  for s, f in zip(s, f):
    activities.append(Activity(s, f))
  print("所有的活动为： {}".format(activities))
  print("最大的兼容活动集为：{}".format(dp_activity_selector(activities)))
  