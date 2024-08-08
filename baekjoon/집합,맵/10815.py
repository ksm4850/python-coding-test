"""
해시맵 저장 시 O(n) 시간복잡도
"""
import sys
input = sys.stdin.readline
N = int(input())

arr1 = list(map(int,input().split()))
M = int(input())

arr2 = list(map(int,input().split()))

dic = {}
for i in range(len(arr1)):
    dic[arr1[i]] = 0


for j in range(len(arr2)):
    if arr2[j] in dic:
        print(1, end=' ')
    else:
        print(0, end=' ')