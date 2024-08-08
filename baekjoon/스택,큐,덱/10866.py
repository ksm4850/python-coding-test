import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

queue = deque()
for _ in range(n):
    i = input().rstrip()

    if i[:10] == 'push_front':
        num = i.split()
        queue.appendleft(num[1])
    if i[:9] == 'push_back':
        num = i.split()
        queue.append(num[1])
    elif i == 'pop_front':
        print(queue.popleft() if queue else -1)
    elif i == 'pop_back':
        print(queue.pop() if queue else -1)
    elif i == 'size':
        print(len(queue))
    elif i == 'empty':
        print(0 if queue else 1)
    elif i == 'front':
        print(queue[0] if queue else -1)
    elif i == 'back':
        print(queue[-1] if queue else -1)