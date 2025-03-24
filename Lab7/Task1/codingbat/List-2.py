#big diff
def big_diff(nums):
  return max(nums) - min(nums)

#centered_average
def centered_average(nums):
    nums.sort()
    return sum(nums[1:-1]) // (len(nums) - 2)

#count_evens
def count_evens(nums):
   return sum(1 for n in nums if n % 2 == 0)

#sum13
def sum13(nums):
    total = 0
    skip = False

    for num in nums:
        if num == 13:
            skip = True
        elif skip:
            skip = False
        else:
            total += num

    return total

#sum67
def sum67(nums):
    total = 0
    in_block = False

    for num in nums:
        if num == 6:
            in_block = True
        elif in_block:
            if num == 7:
                in_block = False
        else:
            total += num

    return total

#has22
def has22(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True
    return False

