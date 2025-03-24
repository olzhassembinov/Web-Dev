#close far
def close_far(a, b, c):
    def close(a, b):
        return abs(a - b) <= 1
    def far(a, b):
        return abs(a - b) >= 2
    return (close(a, b) and far(a, c) and far(b, c)) or (close(a, c) and far(a, b) and far(c, b))

#lone_sum
def lone_sum(a, b, c):
    if a == b == c:
        return 0
    if a == b:
        return c
    if a == c:
        return b
    if b == c:
        return a
    return a + b + c

#lucky_sum
def lucky_sum(a, b, c):
    if a == 13:
        return 0
    if b == 13:
        return a
    if c == 13:
        return a + b
    return a + b + c

#no_teen_sum
def no_teen_sum(a, b, c):
    def fix_teen(n):
        return n if n not in [13, 14, 17, 18, 19] else 0
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

#round_sum
def round_sum(a, b, c):
    def round10(num):
        return (num + 5) / 10 * 10
    return round10(a) + round10(b) + round10(c)

#make_bricks
def make_bricks(small, big, goal):
    return goal % 5 <= small and goal - big * 5 <= small

#make_chocolate
def make_chocolate(small, big, goal):
    if goal >= 5 * big:
        remainder = goal - 5 * big
    else:
        remainder = goal % 5
    if remainder <= small:
        return remainder
    return -1   

