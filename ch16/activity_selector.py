
class Activity:
  """活动的类"""
  def __init__(self, s, f):
    self.s = s
    self.f = f

  def __lt__(self, other):
    return self.f < other.f
  
  def __repr__(self):
    return "{}({}, {})".format(self.__class__.__name__, self.s, self.f)
  
def recursive_activity_selector(activities, k, n):
  m = k + 1
  while m <= n and activities[m].s < activities[k].f:
    m += 1
  if m <= n:
    t = recursive_activity_selector(activities, m, n)
    return [activities[m]] if t is None else [activities[m]] + t
  else:
    return None


def greedy_activity_selector(activities):
  n = len(activities)
  A = activities[0:1]
  k = 0
  for i in range(1, n):
    if activities[i].s >= activities[k].f:
      A.append(activities[i])
      k = i
  return A