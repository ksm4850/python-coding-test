from collections import deque
import sys

# input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = str(input())

    n = int(input())

    arr = input()[1:-1].split(',')

    q = deque(arr)
    R = 0

    if n == 0:
        q = []

    for i in p:
        if i == 'R':
            R += 1
        elif i == 'D':
            if len(q) > 0:
                if R % 2 == 0:
                    q.popleft()
                else:
                    q.pop()
            else:
                print('error')
                break
    else:
        if R % 2 == 0:
            print("[" + ",".join(q) + "]")
        else:
            q.reverse()
            print("[" + ",".join(q) + "]")
        