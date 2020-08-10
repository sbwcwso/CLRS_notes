"""16-1 找零问题"""

def coin_change(d, v):
  """找零问题，需要确保 d 按升序排列"""
  c = [0] * (v + 1)
  b = [0] * (v + 1)
  for i in range(1, v+1):
    c[i] = float('inf')
    for j in range(len(d)):
      if d[j] > i:
        break
      t = 1 + c[i-d[j]]
      if t < c[i]:
        c[i], b[i] = t, j
  construct_solution(d, v, b)


def construct_solution(d, v, b):
  res = [0] * len(d)  # 每种硬币所需要的数量
  while v > 0:
    res[b[v]] += 1
    v -= d[b[v]]
  print("找零选择为：")
  sums = 0
  for i, nums in enumerate(res):
    sums += nums
    if nums > 0:
      print("\t{} 个 {} 美分的硬币".format(nums, d[i]))
  print("总的硬币数量为： ", sums)


if __name__ == "__main__":
  import random
  d = sorted(random.sample(range(100), 10))
  v = random.randint(100, 200)
  print("硬币的面值为： ", d)
  print("总金额为：", v, '美分')
  coin_change(d, v)