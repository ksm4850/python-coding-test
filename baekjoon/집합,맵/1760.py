import sys

input = sys.stdin.readline

N,M = map(int,input().split())

arr1 = [str(input().strip()) for _ in range(N)]
arr2 = [str(input().strip()) for _ in range(M)]

result = list(set(arr1) & set(arr2))
result.sort()
print(len(result))
for i in result:
    print(i)