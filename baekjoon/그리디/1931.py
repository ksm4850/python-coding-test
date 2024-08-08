import sys

input = sys.stdin.readline
n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int,input().split())))

arr.sort(key=lambda x: (x[1],x[0]))

cnt = 0
prev = 0
for start,end in arr:
    if start >= prev:
        cnt += 1
        prev = end

print(cnt)