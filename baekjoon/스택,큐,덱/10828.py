import sys
input = sys.stdin.readline

n = int(input())

stack = []

for _ in range(n):
    i = input().rstrip()

    if i[:4] == 'push':
        num = i.split()
        stack.append(int(num[1]))
    elif i == 'pop':
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif i == 'size':
        print(len(stack))
    elif i == 'empty':
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    elif i == 'top':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
