import sys
input = sys.stdin.readline

n,k = map(int,input().split())
arr = []
for __ in range(n):
  arr.append(int(input().rstrip()))
res = 0
for i in arr[::-1]:
  a = k//i
  if a > 0:
    res += a
    k = k%i

print(res)

