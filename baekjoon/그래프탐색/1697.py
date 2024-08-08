from collections import deque

MAX = int(1e5)
n, k = map(int, input().split())

arr = [0] * (MAX + 1)

q = deque()
q.append(n)

while q:
    x = q.popleft()

    if x == k:
        print(arr[x])
        break

    for nx in (x - 1, x + 1, 2 * x):
        if 0 <= nx <= MAX and arr[nx] == 0:
            arr[nx] = arr[x] + 1
            q.append(nx)
