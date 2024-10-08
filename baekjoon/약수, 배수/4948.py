"""
1 <= n <= 123,456 

에라토스테네스의 체

1. 1은 제거
2. 지워지지않은 수 중 제일 작은 2를 소수로 채택하고 2의 배수를 모두 지움
3. 지워지지않은 수 중 제일 작은 3을 소수로 채택하고 3의 배수를 모두 지움
4. 반복
"""
check = [0] * 2 + [1] * 246912 # 0 1

#첫 소수만 1로 남기고
#소수의 배수들은 소수가 아니므로 0으로 초기화
for i in range(2, 246913):
    if check[i]:
        for j in range(i * 2, 246913, i):
            check[j] = 0

while True:
    x = int(input())
    if x == 0:
        break
    print(sum(check[x+1:x*2+1]))