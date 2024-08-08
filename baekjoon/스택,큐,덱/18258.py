import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

q = deque()

for _ in range(N):
    i = input().rstrip()

    if i[:4] == 'push':
        num = i.split()
        q.append(int(num[1]))
    elif i == 'pop':
        print(q.popleft() if q else -1)
    elif i == 'size':
        print(len(q))
    elif i == 'empty':
        print(0 if q else 1)
    elif i == 'front':
        print(q[0] if quit else -1)
    elif i == 'back':
        print(q[-1] if q else -1)