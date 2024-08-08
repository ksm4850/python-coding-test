
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()

print(round(sum(arr)/len(arr)))

print(arr[len(arr)//2])

fre = {}

for i in arr:
    if i in fre:
        fre[i] += 1
    else:
        fre[i] = 1

max_fre = max(fre.values())
most_common_val = [key for key in fre if fre[key] == max_fre]

if len(most_common_val) > 1:
    print(most_common_val[1])
else:
    print(most_common_val[0])

print(arr[-1] - arr[0])