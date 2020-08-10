"""16.1-4 区间图着色问题"""
from ch16.activity_selector import greedy_activity_selector, Activity


def activities_arrange(activities):
  """借助寻找最大兼容子集的方法来求解"""
  current_activities = list(activities)
  rooms = []
  while current_activities:
    rooms.append(greedy_activity_selector(current_activities))
    remain_activities = []
    for activity in current_activities:
      if activity not in rooms[-1]:
        remain_activities.append(activity)
    current_activities = remain_activities
  return rooms


if __name__ == "__main__":
  s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
  f = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
  activities = []
  for s, f in zip(s, f):
    activities.append(Activity(s, f))
  print("所有的活动为： {}".format(activities))
  print("各个教室中的活动为：\n{}".format("\n".join(repr(item) for item in activities_arrange(activities))))
  