#1
if __name__ == '__main__':
    print("Hello, World!")

#2
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 == 1:
        print("Weird")
    elif n % 2 == 0 and 2 <= n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")

#3
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)

#4
if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(a // b)

    print(a / b)

#5
if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        print(i ** 2)

#6
def is_leap(year):
    leap = False

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True

    return leap

year = int(input())
print(is_leap(year))

#7
if __name__ == '__main__':
    n = int(input())

    for i in range(1, n+1):
        print(i, end="")

#8
x, k = map(int, input().split())

polynomial = input()

print(eval(polynomial) == k)

#9
expression = input()

eval(expression)

#10
n = int(input())
nums = list(map(int, input().split()))
print(all(i > 0 for i in nums) and any(str(i) == str(i)[::-1] for i in nums))

