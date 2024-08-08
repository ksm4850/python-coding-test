import sys

input = sys.stdin.readline
N = int(input())
stack = []
for _ in range(N):
    x = input().rstrip()
    if len(x) > 2:
        stack.append(int(x[2:]))
    elif x == '2':
        print(-1 if len(stack) == 0 else stack.pop())
    elif x == '3':
        print(len(stack))
    elif x == '4':
        print(1 if len(stack) == 0 else 0)
    elif x == '5':
        print(-1 if len(stack) == 0 else stack[-1])



