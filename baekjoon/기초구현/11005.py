N, B = map(int, input().split())
s = ''
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# N이 0이될때까지 반복
while N:
    s += str(arr[N%B])
    N //= B 

print(s[::-1])

