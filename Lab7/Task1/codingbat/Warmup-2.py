#array123
def array123(nums):
    for i in range(len(nums)-2):
        if nums[i:i+3] == [1,2,3]:
            return True
    return False

#string_times
def string_times(str, n):
    return str*n

#front_times
def front_times(str, n):
    return str[:3]*n   

#string_bits
def string_bits(str):
    return str[::2]

#string_splosion
def string_splosion(str):
    return ''.join([str[:i] for i in range(1,len(str)+1)])

#last2
def last2(str):
    count = 0
    for i in range(len(str)-2):
        if str[i:i+2] == str[-2:]:
            count += 1
    return

#array_count9
def array_count9(nums):
    return nums.count(9)

#array_front9
def array_front9(nums):
    return 9 in nums[:4]

#string_match
def string_match(a, b):
    return sum([a[i:i+2] == b[i:i+2] for i in range(len(a)-1)])

