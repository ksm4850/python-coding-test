
X = int(input())

cnt = 0

arr = [64,32,16,8,4,2,1]

for i in arr:
    if i <= X:
        X -= i
        cnt += 1
    if X == 0:
        break
print(cnt)