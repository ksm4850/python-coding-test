N, K = map(int, input().split())
tmp = 0
sieve = [True] * (N + 1) # 소수판별
for i in range(2, N + 1):
    for j in range(i, N + 1, i):
        # 2부터 차례대로 자신의 배수를 모두 지워나감
        if sieve[j] != False:
            sieve[j] = False
            tmp += 1
            if tmp == K:
                print(j)