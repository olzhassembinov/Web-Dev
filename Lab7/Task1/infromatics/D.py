#a
N = int(input())
arr = list(map(int, input().split()))

print(*arr[::2])

#b
N = int(input())
arr = list(map(int, input().split()))

for num in arr:
    if num % 2 == 0:
        print(num, end=" ")

#c
N = int(input())
arr = list(map(int, input().split()))

count = 0
for num in arr:
    if num > 0:
        count += 1

print(count)

#d
N = int(input())
arr = list(map(int, input().split()))

count = 0
for i in range(1, N):
    if arr[i] > arr[i - 1]:
        count += 1

print(count)

#e
N = int(input())

arr = list(map(int, input().split()))

found = False

for i in range(1, N):
    if (arr[i] > 0 and arr[i-1] > 0) or (arr[i] < 0 and arr[i-1] < 0):
        found = True
        break

if found:
    print("YES")
else:
    print("NO")

#f
N = int(input())
arr = list(map(int, input().split()))

count = 0

for i in range(1, N-1):
    if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
        count += 1

print(count)

#g
N = int(input())
arr = list(map(int, input().split()))

for i in range(N // 2):
    arr[i], arr[N - i - 1] = arr[N - i - 1], arr[i]

print(*arr)