N, K = map(int, input().split())

arr = [i+1 for i in range(N)]
c = 0
result = []
while len(arr) > 0:
    c = (c + (K-1)) % len(arr)
    cc = arr.pop(c)
    result.append(str(cc))

print("<%s>" %(", ".join(result)))