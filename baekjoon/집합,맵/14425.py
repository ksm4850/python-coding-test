"""
N : 집합 문자열 갯수
M : 검사해야할 문자 갯수

S : 집합문자
"""

import sys

input = sys.stdin.readline
N,M = map(int,input().split())

S = set()

for _ in range(N):
    S.add(str(input().strip()))

cnt = 0
for _ in range(M):
    chk = str(input().strip())
    if chk in S:
        cnt += 1
print(cnt)