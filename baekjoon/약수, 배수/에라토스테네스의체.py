"""
에라토스테네스의 체

1. 1은 제거
2. 지워지지않은 수 중 제일 작은 2를 소수로 채택하고 2의 배수를 모두 지움
3. 지워지지않은 수 중 제일 작은 3을 소수로 채택하고 3의 배수를 모두 지움
4. 반복
"""
n = 1000
a = [False, False] + [True] * (n - 1)
primes = []

for i in range(2, n + 1):
    if a[i]:
        primes.append(i)
        for j in range(2 * i, n + 1, i): # i의 배수를 모두 지움
            a[j] = False
print(primes)