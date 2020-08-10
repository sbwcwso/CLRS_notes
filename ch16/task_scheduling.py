from collections import namedtuple
import bisect
from operator import attrgetter


class Task:
  def __init__(self, d, w):
    self.d = d
    self.w = w

  def __repr__(self):
    class_name = type(self).__name__
    return "{}({!r}, {!r})".format(class_name, self.d, self.w)


def task_scheduling(tasks):
  """单任务时间调度，假设任务已按惩罚时间单调递减的顺序排序"""

  N = [0] * len(tasks)  #　储存 N_t 的值
  tasks = sorted(tasks, key=attrgetter('w'), reverse=True)
  early_tasks, late_tasks = [], []
  w = 0
  for task in tasks:
    tmp = N[:] # 复制 N，防止延迟任务更新 N
    i = task.d - 1
    while i < len(tasks):
      tmp[i] += 1
      if tmp[i] > i + 1:
        late_tasks.append(task)
        w += task.w
        break
      i += 1
    if i == len(tasks):
      early_tasks.append(task)
      N = tmp
  
  return sorted(early_tasks, key=attrgetter('d')) + late_tasks, w


if __name__ == "__main__":
  tasks = []
  for d, w in zip([4, 2, 4, 3, 1, 4, 6], [70, 60, 50, 40, 30, 20, 10]):
   tasks.append(Task(d, w))
  print("任务为： \n", "\n".join(repr(task) for task in tasks), sep='')
  res, w = task_scheduling(tasks)
  print("最终的任务调度序列为: \n", "\n".join(repr(task) for task in res), sep='')
  print("总的超时惩罚为: ", w)