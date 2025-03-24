#a
import math

a = int(input())
b = int(input())

c = math.sqrt(a**2 + b**2)

print(c)

#b
n = int(input())

print("The next number for the number", n, "is", n + 1, end=".\n")
print("The previous number for the number", n, "is", n - 1, end=".")

#c
N = int(input())
K = int(input())

apples_per_student = K // N

print(apples_per_student)

#d
N = int(input())
K = int(input())

remaining_apples = K % N

print(remaining_apples)

#e
v = int(input())
t = int(input())

position = (v * t) % 109

if position < 0:
    position += 109

print(position)