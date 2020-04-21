"""16.1-4 区间图着色问题"""
from ch16.activity_selector import greedy_activity_selector


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