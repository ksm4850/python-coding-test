"""
n보다 크거나 가은 소수 중 가장 작은 소수 찾기

소수 : 1과 자기자신으로만 나눠지는 수
"""

import sys
import math

def check(n):
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True # 소수
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    num = int(input())
    while True:
        if num == 0 or num == 1:
            print(2)
            break
        
        if check(num):
            print(num)
            break
        else:
            num += 1
        
