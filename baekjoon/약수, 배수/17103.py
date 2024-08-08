"""
짝수 N을 두 소수의 합으로 나타내는 표현

에라토스테네스의 체로 모든 소수를 찾은다음

입력수 - 찾은 소수 == 소수면 골드바흐 파티션

"""
import sys

prime = [] # 소수가 들어갈 배열
check = [0] * 1000001
# 0과 1 소수처리
check[0] = 1  
check[1] = 1

# 100만 이하 중 소수 찾기
for i in range(2, 1000001):
    if check[i] == 0:
        prime.append(i)
        # i의 배수는 전부 짝수
        for j in range(2*i, 1000001, i):
            check[j] = 1

T = int(sys.stdin.readline())

for _ in range(T):
    count = 0
    N = int(sys.stdin.readline())
    for i in prime:
        if i >= N:
            break
        if not check[N - i] and i <= N-i:  # 순서만 다른거 counting 하지 않기 위해
            count += 1
    print(count)