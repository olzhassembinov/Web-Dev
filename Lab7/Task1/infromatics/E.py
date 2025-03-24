#a
def min_four(a, b, c, d):
    return min(a, b, c, d)

a, b, c, d = map(int, input().split())

print(min_four(a, b, c, d))

#b
def power(a, n):
    result = 1
    for _ in range(n):
        result *= a
    return result

a, n = input().split()
a = float(a)
n = int(n)

print(power(a, n))

#c
def xor(x, y):
    return (x and not y) or (not x and y)

x, y = map(int, input().split())

print(1 if xor(bool(x), bool(y)) else 0)