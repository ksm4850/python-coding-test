M = int(input())
N = int(input())
sosu = 0
num_list = []
for i in range(M,N+1):
    if i > 1:
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            sosu += 1
            num_list.append(i)

if sosu == 0:
    print(-1)
else:
    print(sum(num_list))
    print(min(num_list))
