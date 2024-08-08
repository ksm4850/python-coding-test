"""
arr1 = 가지고있는 카드 

arr2 = 몇개가지고있는지 구해야할 정수


"""
import sys
input = sys.stdin.readline
N = int(input())
arr1 = list(map(int,input().split()))
dic = {}

M = int(input())
arr2 = list(map(int,input().split()))

for n in arr1:
    if n in dic:
        dic[n] += 1
    else:
        dic[n] = 1

# result = []
# for m in arr2:
#     if m in dic:
#         print(dic[m],end=' ')
#     else:
#         print(0,end=' ')
print(' '.join(str(dic[m]) if m in dic else '0' for m in arr2))