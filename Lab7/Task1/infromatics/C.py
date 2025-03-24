#ia
a = int(input())
b = int(input())

for i in range(a, b + 1):
    if i % 2 == 0:
        print(i, end=" ")

#ib
a = int(input())
b = int(input())
c = int(input())
d = int(input())

for i in range(a, b + 1):
    if i % d == c:
        print(i, end=" ")

#ic
a = int(input())
b = int(input())

for i in range(a, b + 1):
    if int(i**0.5)**2 == i:
        print(i, end=" ")

#id
x = input()
d = input()

count = x.count(d)

print(count)

#ie
x = input()

total = sum(int(digit) for digit in x)

print(total)

#ig
x = int(input())

for i in range(2, x + 1):
    if x % i == 0:
        print(i)
        break

#ih
x = int(input())

for i in range(1, x + 1):
    if x % i == 0:
        print(i, end=" ")

#ii
import math

x = int(input())
count = 0

for i in range(1, int(math.sqrt(x)) + 1):
    if x % i == 0:
        count += 1
        if i != x // i:
            count += 1

print(count)

#ij
total = 0

for _ in range(100):
    total += int(input())

print(total)

#ik
N = int(input())
total = 0

for _ in range(N):
    total += int(input())

print(total)

#il
binary_number = input()

decimal_number = int(binary_number, 2)

print(decimal_number)

#im
N = int(input())

zero_count = 0

for _ in range(N):
    number = int(input())
    if number == 0:
        zero_count += 1

print(zero_count)

#iia
N = int(input())

i = 1
while i * i <= N:
    print(i * i)
    i += 1

#iib
N = int(input())

for i in range(2, N + 1):
    if N % i == 0:
        print(i)
        break

#iic
N = int(input())

power = 1
while power <= N:
    print(power, end=" ")
    power *= 2

#iid
N = int(input())

power = 1
while power < N:
    power *= 2

if power == N:
    print("YES")
else:
    print("NO")

#iie
N = int(input())

k = 0
power = 1

while power < N:
    power *= 2
    k += 1

print(k)