from collections import deque

n = int(input())

for _ in range(n):
    N,M = map(int, input().split())
    queue = deque(map(int, input().split()))
    cnt = 0

    while queue:
        best = max(queue)
        front = queue.popleft()

        M -= 1

        if best == front:
            cnt += 1
            if M < 0: break
        else:
            queue.append(front)
            if M < 0:
                M = len(queue) - 1
    print(cnt)