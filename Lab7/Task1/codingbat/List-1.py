#common end
def common_end(a, b):
  return a[0] == b[0] or a[-1] == b[-1]

#firs last 6
def first_last6(nums):
  return nums[0] == 6 or nums[-1] == 6

#has 23
def has23(nums):
  return 2 in nums or 3 in nums

#make ends
def make_ends(nums):
  return [nums[0], nums[-1]]

#make pi
def make_pi():
  return [3, 1, 4]

#max end 3
def max_end3(nums):
  max_val = max(nums[0], nums[2])
  return [max_val] * 3

#middle way
def middle_way(a, b):
  return [a[1], b[1]]

#reverse 3
def reverse3(nums):
  return [nums[2], nums[1], nums[0]]

#sum 2
def sum2(nums):
  if len(nums) == 0:
    return 0
  elif len(nums) < 2:
    return nums[0]
  else:
    return nums[0] + nums[1]
  
#sum 3
def sum3(nums):
  return sum(nums)