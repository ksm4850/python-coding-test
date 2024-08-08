n = int(input())

result = 0
num = map(int,input().split())
for i in num:
    cnt = 0
    if i > 1:
        for j in range(2,i):
            if i%j == 0:
                cnt += 1
                break

        if cnt == 0:
            result += 1

print(result)
