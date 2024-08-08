import sys
sys.setrecursionlimit(int(1e6)) # 재귀함수 한계 풀어줌

n = int(input())

def fac(num):
    if num == 0:
        return 1
    return num * fac(num-1)

print(fac(n))