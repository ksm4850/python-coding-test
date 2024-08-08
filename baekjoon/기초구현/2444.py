n = int(input())
for i in range(1, n):
    print(' '*(n-i) + '*'*(2*i-1))
for i in range(n, 0, -1): # start, stop, step
    print(' '*(n-i) + '*'*(2*i-1))