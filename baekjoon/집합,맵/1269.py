"""
차집합 갯수 구하기
"""

import sys

input = sys.stdin.readline

N,M = map(int,input().strip().split())

arr1 = input().split()
arr2 = input().split()

cha1 = list(set(arr1) - set(arr2))
cha2 = list(set(arr2) - set(arr1))

print(len(cha1) + len(cha2))


